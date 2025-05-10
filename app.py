import cv2
import mediapipe as mp
import numpy as np
from deepface import DeepFace
from flask import Flask, render_template, Response, jsonify, request, redirect, url_for, flash
import base64
import threading
import pyttsx3  # voice assistant
import time
import secrets

from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash

last_emotion_analysis_time = 0
video_feed_active = True

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = secrets.token_hex(32)  # Generates a 64-character hex string

# Initialize Flask extensions
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    snapshots = db.relationship('Snapshot', backref='user', lazy=True)

# Snapshot model
class Snapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_data = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    min_detection_confidence=0.3  # Lower confidence threshold
)

current_frame = None
frame_with_hairstyle = None
frame_lock = threading.Lock()
voice_enabled = True  # Default: Voice assistant is enabled

analysis_results = {
    'face_shape': 'Unknown',
    'emotion': 'Neutral',
    'hairstyle_options': [],
    'current_hairstyle': None
}

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Hairstyles
HAIRSTYLES = {
    'short_spiky': {
        'image_path': 'static/hairstyles/short_spiky.png',
        'overlay_pos': (0.35, 0.1),
        'suitable_for': ['Oval', 'Square']
    },
    'long_straight': {
        'image_path': 'static/hairstyles/long_straight.png',
        'overlay_pos': (0.3, 0.05),
        'suitable_for': ['Oval', 'Heart']
    },
    'curly_bob': {
        'image_path': 'static/hairstyles/curly_bob.png',
        'overlay_pos': (0.35, 0.15),
        'suitable_for': ['Round', 'Heart']
    },
    'pixie_cut': {
        'image_path': 'static/hairstyles/pixie_cut.png',
        'overlay_pos': (0.4, 0.2),
        'suitable_for': ['Oval', 'Heart']
    },
    'afro': {
        'image_path': 'static/hairstyles/afro.png',
        'overlay_pos': (0.3, 0.1),
        'suitable_for': ['Oval', 'Square']
    }
}

# Load hairstyle images
for name, data in HAIRSTYLES.items():
    data['image'] = cv2.imread(data['image_path'], cv2.IMREAD_UNCHANGED)
    if data['image'] is None:
        print(f"[ERROR] Could not load image for '{name}'")

def calculate_distance(p1, p2):
    return np.linalg.norm([p1.x - p2.x, p1.y - p2.y])
def detect_face_shape(landmarks, w, h):
    try:
        jaw_w = calculate_distance(landmarks[0], landmarks[16]) * w
        face_h = calculate_distance(landmarks[10], landmarks[152]) * h
        cheek_w = calculate_distance(landmarks[234], landmarks[454]) * w

        j2h = jaw_w / face_h if face_h else 0
        c2h = cheek_w / face_h if face_h else 0
        h2j = face_h / jaw_w if jaw_w else 0

        if j2h > 1.3 and c2h < 1.1:
            return "Square"
        elif c2h > 1.2 and j2h < 1.2:
            return "Round"
        elif c2h > 1.1 and j2h < 1.1:
            return "Heart"
        elif h2j > 1.5:
            return "Oval"
        else:
            return "Unknown"
    except:
        return "Unknown"

def get_suitable_hairstyles(shape, emotion):
    styles = []
    for name, data in HAIRSTYLES.items():
        if shape in data['suitable_for']:
            styles.append({
                'name': name,
                'display_name': name.replace('_', ' ').title(),
                'image_url': f"/static/hairstyles/{name}.png"
            })
    if emotion.lower() in ['happy', 'surprise']:
        styles = [s for s in styles if s['name'] in ['short_spiky', 'curly_bob', 'afro']]
    elif emotion.lower() in ['sad', 'fear']:
        styles = [s for s in styles if s['name'] in ['long_straight', 'pixie_cut']]
    return styles[:4]

def apply_hairstyle_overlay(frame, landmarks, name):
    if name not in HAIRSTYLES:
        return frame
    hdata = HAIRSTYLES[name]
    overlay = hdata['image']
    if overlay is None:
        return frame

    x_min = int(min([lm.x for lm in landmarks]) * frame.shape[1])
    y_min = int(min([lm.y for lm in landmarks]) * frame.shape[0])
    x_max = int(max([lm.x for lm in landmarks]) * frame.shape[1])
    y_max = int(max([lm.y for lm in landmarks]) * frame.shape[0])
    f_w = x_max - x_min
    f_h = y_max - y_min

    new_w = int(f_w * 1.5)
    new_h = int(new_w * overlay.shape[0] / overlay.shape[1])
    overlay = cv2.resize(overlay, (new_w, new_h))

    pos_x = max(0, x_min - int(hdata['overlay_pos'][0] * f_w))
    pos_y = max(0, y_min - int(hdata['overlay_pos'][1] * f_h) - int(new_h * 0.6))
    end_x = min(frame.shape[1], pos_x + new_w)
    end_y = min(frame.shape[0], pos_y + new_h)

    alpha = overlay[:, :, 3] / 255.0
    overlay_rgb = overlay[:, :, :3]

    for c in range(3):
        frame[pos_y:end_y, pos_x:end_x, c] = (
            alpha[:end_y - pos_y, :end_x - pos_x] * overlay_rgb[:end_y - pos_y, :end_x - pos_x, c] +
            (1 - alpha[:end_y - pos_y, :end_x - pos_x]) * frame[pos_y:end_y, pos_x:end_x, c]
        )
    return frame

def process_frame(frame):
    global current_frame, frame_with_hairstyle, last_emotion_analysis_time
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for face in result.multi_face_landmarks:
            landmarks = face.landmark
            shape = detect_face_shape(landmarks, frame.shape[1], frame.shape[0])

            # Perform emotion analysis every 5 seconds
            if time.time() - last_emotion_analysis_time > 5:
                try:
                    x1 = int(min([lm.x for lm in landmarks]) * frame.shape[1])
                    y1 = int(min([lm.y for lm in landmarks]) * frame.shape[0])
                    x2 = int(max([lm.x for lm in landmarks]) * frame.shape[1])
                    y2 = int(max([lm.y for lm in landmarks]) * frame.shape[0])
                    face_img = frame[y1:y2, x1:x2]
                    result = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
                    emotion = result[0]['dominant_emotion']
                    last_emotion_analysis_time = time.time()
                except:
                    emotion = "Neutral"

                with frame_lock:
                    analysis_results['emotion'] = emotion

            with frame_lock:
                analysis_results['face_shape'] = shape
                analysis_results['hairstyle_options'] = get_suitable_hairstyles(shape, analysis_results['emotion'])

                if analysis_results['current_hairstyle']:
                    frame = apply_hairstyle_overlay(frame, landmarks, analysis_results['current_hairstyle'])
                    if voice_enabled:
                        speak(f"Showing you the {analysis_results['current_hairstyle'].replace('_', ' ')} style")

    with frame_lock:
        current_frame = frame.copy()
        frame_with_hairstyle = frame.copy()
    return frame

def generate_frames():
    global video_feed_active
    cap = cv2.VideoCapture(0)
    while video_feed_active:
        success, frame = cap.read()
        if not success:
            break
        # Resize frame to reduce resolution
        frame = cv2.resize(frame, (640, 480))
        frame = process_frame(frame)
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    cap.release()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/try-on')
@login_required
def try_on():
    return render_template('index.html')
@app.route('/index')
def index():
    return redirect(url_for('home'))  # or whatever you want this route to do

@app.route('/profile')
@login_required
def profile():
    user_snapshots = Snapshot.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', snapshots=user_snapshots)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_analysis')
def get_analysis():
    with frame_lock:
        return jsonify(analysis_results)

@app.route('/set_hairstyle/<hairstyle>')
def set_hairstyle(hairstyle):
    global voice_enabled
    voice_enabled_param = request.args.get("voice", "true").lower()
    voice_enabled = (voice_enabled_param == "true")

    with frame_lock:
        analysis_results['current_hairstyle'] = hairstyle if hairstyle != 'none' else None
    return jsonify({'status': 'success'})

@app.route('/take_snapshot')
@login_required
def take_snapshot():
    with frame_lock:
        if frame_with_hairstyle is not None:
            _, buffer = cv2.imencode('.jpg', frame_with_hairstyle)
            snapshot = base64.b64encode(buffer).decode('utf-8')
            new_snapshot = Snapshot(image_data=snapshot, user_id=current_user.id)
            db.session.add(new_snapshot)
            db.session.commit()
            return jsonify({
                'snapshot': snapshot,
                'profile_url': url_for('profile')
            })
        return jsonify({'snapshot': None})

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another.')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You are now logged in.')
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data (using 'username' since that's what's used in registration)
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validate input
        if not username or not password:
            flash('Please fill in all fields', 'error')
            return redirect(url_for('login'))
        
        # Find user
        user = User.query.filter_by(username=username).first()
        
        # Check user exists and password matches
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.')
    return redirect(url_for('home'))

@app.route('/buy_product/<product_id>', methods=['POST'])
@login_required
def buy_product(product_id):
    # Simulate a purchase process (e.g., save to database or call payment API)
    flash(f'Product {product_id} purchased successfully!')
    return redirect(url_for('profile'))

@app.route('/stop_video_feed', methods=['POST'])
def stop_video_feed():
    global video_feed_active
    video_feed_active = False  # Stop the video feed loop
    # Add any additional cleanup code here if needed
    return jsonify({'status': 'success'})

@app.route('/book_barbershop/<int:barber_id>')
def book_barbershop(barber_id):
    # Add logic to book a barbershop appointment
    return f"Booking barbershop with id: {barber_id}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5501, threaded=True)