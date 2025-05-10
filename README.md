# Looksy-A-virtual-hairstyle-try-on
![Screenshot 2025-05-08 224351](https://github.com/user-attachments/assets/66bc8bea-0654-450c-bf6e-48b629abef9a)
![Screenshot 2025-05-08 224411](https://github.com/user-attachments/assets/04e3ea7e-4b4d-4175-8a1a-253b75b0ab21)
![Screenshot 2025-05-08 224432](https://github.com/user-attachments/assets/ca5a5836-ab38-416f-983d-4fd734731c3f)
![Screenshot 2025-05-08 224455](https://github.com/user-attachments/assets/dfb57389-3c79-47ab-b8ae-774333ca76f4)
![Screenshot 2025-05-08 224519](https://github.com/user-attachments/assets/6f5d7ded-85de-4068-882b-5c9149adbc23)
![Screenshot 2025-05-08 224632](https://github.com/user-attachments/assets/bc103652-e71e-4294-8b01-10eb28fda525)
![Screenshot 2025-05-08 224703](https://github.com/user-attachments/assets/e00a5a6d-cd72-4870-aa32-06e23d1f0c13)
![Screenshot 2025-05-08 224739](https://github.com/user-attachments/assets/68af9284-a96a-4cc1-ae18-f723b628d791)
![Screenshot 2025-05-08 224928](https://github.com/user-attachments/assets/0436119d-6fdf-40ab-aa3c-67cacc973e83)
![framework diagram](https://github.com/user-attachments/assets/4bdb71d6-6201-4a4c-9593-18adb8f132c3)
![deepseek_mermaid_20250507_a4edfe](https://github.com/user-attachments/assets/20c89727-ee5a-4e19-b433-a4eb02a527a6)

CHAPTER-1 
INTRODUCTION
The "Looksy : A virtual hairstyle try-on" project is a web application that allows 
users to try on different hairstyles based on their face shape and emotional state. It uses 
real-time face detection, overlays hairstyle images, and recommends styles that suit a user's 
unique features. The system aims to assist users in making better grooming and styling 
decisions using AI technologies.
The Looksy : A Virtual hairstyle try-on is designed to provide intelligent, face-shape-based 
hairstyle suggestions to users through a web platform. By analyzing the user's facial features 
from a photograph, the system identifies the face shape using deep learning algorithms.
Based on this analysis, it matches the face shape with suitable hairstyles stored in the 
system’s database and generates tailored recommendations.
This project combines the power of artificial intelligence, computer vision, and modern web 
technologies. The frontend of the application is built using React to ensure a smooth and 
interactive user experience. The backend, developed in Python, handles face shape
detection, business logic, and database interactions. The data is stored in a structured
manner using MySQL, and an admin panel allows for the management of hairstyle data.
The system benefits not only individual users but also salons and hairstylists who wish to 
offer personalized style suggestions. It demonstrates how modern technologies can be 
leveraged to improve user experience in the fashion and grooming industry.
Choosing the right hairstyle can be challenging without expert advice or visualization tools. 
Users lack an interactive, real-time system that understands their facial structure and 
emotions to recommend hairstyles. Traditional salon consultations are limited in time and 
resources, making an automated, intelligent recommendation system both necessary and 
valuable.
This project combines several cutting-edge technologies to deliver its functionality:
 Computer Vision & AI: Tools like MediaPipe and OpenCV are used to detect facial 
landmarks and analyse the facial structure. Face shape classification is powered by 
pre-trained CNN’s learning models capable of distinguishing between common 
shapes such as Oval, Round, Square, and Heart.
 Frontend Development
1.core framework & libraries
 Html5 & css3
 JavaScript(Es6+)
 fetch Api:- ajax
 Dom manipulation
2. Ui/ux enhancement
 bootstrap5
 font awesome
 animate.css
3. Real time video processing
 canvas Api
 media Stream Api
Backend Development:
1. Core Framework
Flask (Python): Lightweight, flexible, and ideal for prototyping.
2. Key Routes
 video feed: Streams processed video frames.
 set hairstyle: Handles hairstyle selection.
 take snapshot: Saves images to the database.
3. ai/ computer vision
 OpenCV
 media pipe
 deepface
4. Database & authentication
 SQLite
 Table & user
 Flask login
 Password hashing
5. APIs & communication
 additional backend tools
 Pyttsx3
 threading
 Admin Panel: An administrator interface enables content management, including 
the addition, deletion, and categorization of hairstyle data for future expansion.
1.1 OBJECTIVE
To develop a user-friendly online interface for hairstyle recommendation. 
To perform real-time face shape and emotion detection.
To recommend hairstyles based on AI logic. 
To integrate voice assistance for accessibility.
To enable user registration and profile-based customization.
The primary objective of this project is to develop a smart, web-based Looksy : A Virtual 
hairstyle try-on that uses artificial intelligence and computer vision to provide personalized 
hairstyle suggestions based on a user's facial features and face shape. The system is designed
to enhance user experience by allowing individuals to make confident hairstyle decisions 
without relying solely on subjective advice or trial and error.
Specific Objectives:
1. Face Detection and Analysis
To accurately detect the user's face from a photograph or real-time webcam input 
using computer vision libraries such as OpenCV and MediaPipe. The system should 
identify facial landmarks and key regions of the face (e.g., jawline, cheekbones, 
forehead) to assist in the classification of face shapes.
2. Face Shape Classification
To implement a reliable algorithm that classifies detected facial structures into 
standard face shapes, such as Oval, Round, Square, and Heart. This classification 
serves as the foundation for hairstyle recommendations.
3. Admin Panel for Hairstyle Management
To provide administrators with a backend dashboard for managing hairstyle data, 
updating images, editing metadata, and adding new styles based on trends and user 
feedback.
4. Scalability and Future Enhancements
To design the system architecture in a modular and scalable way so that additional 
features (e.g., hair color simulation, gender-based styles, emotion-based suggestions) 
can be easily integrated in future versions.
1.2 MOTIVATION
The motivation behind this project is to simplify and personalize the hairstyle selection 
process. Choosing the right hairstyle can be confusing, and many people are unsure what
suits them best. By using face detection and AI-based emotion analysis, this system bridges 
the gap between technology and personal grooming.
Traditionally, hairstyle recommendations have relied on the intuition of stylists or general 
advice found in magazines and websites. These methods are not personalized and often fail to 
consider the unique facial structure of each individual. Moreover, the lack of real-time 
visualization tools forces users to rely on imagination or guesswork, leading to uncertainty 
and poor decisions.
With advancements in artificial intelligence, computer vision, and web development, there is 
an opportunity to bridge this gap through automation and personalization. The motivation 
behind this project arises from the desire to create an intelligent system that simplifies the 
hairstyle selection process using facial analysis and modern technology.
By developing a system that detects face shape and suggests suitable hairstyles, users can 
explore options confidently and efficiently. Additionally, the integration of AR technology to 
preview hairstyles in real-time adds an engaging and futuristic touch to the user experience. 
This not only empowers individuals but also provides value to salon professionals who wish 
to offer digital consultations to their clients.
The project is inspired by the growing demand for personalized digital services and the 
increasing role of AI in enhancing everyday decision-making. It seeks to demonstrate how 
technology can be used to solve practical, relatable problems and improve quality of life by 
merging fashion with intelligent systems.
Furthermore, the increasing popularity of virtual try-on applications in the beauty industry 
shows a clear shift toward interactive, AI-powered solutions. Users today expect more 
control, convenience, and personalization in the services they use. This project aligns with 
those expectations and aims to transform a common grooming challenge into a smart, tech￾enabled experience.
CHAPTER -2 
BACKGROUND
This project combines image processing, emotion detection, and web development. It uses 
OpenCV and Mediapipe to process facial landmarks and DeepFace for emotion analysis. The 
Python Flask framework enables smooth integration between frontend and backend. The 
interface is styled for a modern user experience using HTML/CSS.
Traditionally, professional hairstylists have used their experience and aesthetic judgment to 
recommend hairstyles based on a client's facial structure. However, such consultations are 
limited by time, availability, and human bias. In many cases, clients rely on trial and error, 
leading to dissatisfaction or a reluctance to experiment with new styles. Furthermore, with the 
growing demand for virtual and at-home grooming solutions, the need for intelligent digital 
tools has become more apparent.
With the advancement of artificial intelligence (AI), machine learning, and computer vision, 
new possibilities have emerged for solving practical problems in the fashion and beauty 
industry. Technologies like facial recognition, face mesh detection, and real-time image 
processing are being widely adopted in areas such as virtual makeup, eyewear try-ons, and 
cosmetic surgery previews. These same technologies can be leveraged to create systems that 
analyse facial features and suggest hairstyles accordingly.
Several mobile apps and websites offer basic hairstyle try-on features by allowing users to 
overlay static images on their photos. However, most of these solutions lack intelligence, 
real-time feedback, and customization based on actual face shape analysis. They often fail to 
consider the proportions and dimensions of the user's face, resulting in unrealistic previews 
and poor user experience.
The integration of computer vision techniques such as Media Pipe face mesh and emotion 
detection through DeepFace enables more accurate and meaningful analysis of facial features. 
When combined with a well-designed user interface and backend recommendation engine, 
this technology can deliver a personalized, interactive, and helpful tool for hairstyle selection.
This project builds on these technological advancements to create a fully functional web￾based Looksy : A Virtual hairstyle try-on. By providing a data-driven, real-time, and visually 
engaging solution, it aims to enhance the user’s confidence and simplify the decision-making 
process when choosing a hairstyle. It also opens the door for future integrations in salon 
software and beauty-tech platforms, further expanding its real-world relevance.
2.1 COMPLEXITY OF THE PROBLEM
Accurate face shape detection under varying lighting conditions. 
Emotion detection based on webcam input in real-time.
Overlaying transparent hairstyle images on moving faces. 
Maintaining performance and low latency during video feed.
One of the primary challenges is accurate face shape detection. Human faces vary 
significantly in terms of proportions, angles, and features, making it difficult to categorize 
them into a limited set of face shapes (e.g., oval, round, square, heart, etc.) using fixed 
geometric rules. Small variations in lighting, facial expression, camera angle, or image 
resolution can affect the outcome of detection. To overcome this, robust computer vision 
algorithms and facial landmark detection models like Media Pipe or Dlib are required to 
identify key facial points with high precision.
Another major challenge is the integration of machine learning or rule-based models to 
classify face shapes from detected features. Unlike standard object classification tasks, face 
shape classification lacks universally agreed-upon datasets, and the distinctions between 
categories are often subtle. Developing or training models to recognize these nuanced 
differences adds to the problem's complexity.
Additionally, the system must ensure aesthetic and meaningful hairstyle 
recommendations, which requires a carefully curated and tagged dataset. Hairstyles must be 
associated with face shapes based on expert guidelines or research, and the matching logic
must consider not just face shape, but also alignment, hair volume, gender, and in advanced 
cases, emotional context or user preferences. Mapping these abstract criteria into computable 
parameters is a non-trivial task.
From a system design perspective, real-time AR overlay functionality adds another layer of 
complexity. The system must superimpose hairstyles onto the user’s face in a live video 
stream, maintaining correct alignment, scale, and proportions as the user moves. This 
requires real-time processing, minimal latency, and seamless performance, which poses 
technical challenges in both frontend and backend implementation.
Lastly, ensuring a user-friendly, responsive, and accessible interface that works across 
devices and browsers, while simultaneously handling real-time video input, backend 
processing, and database interactions, requires careful planning and optimization.
Chapter -3 
LITERATURE SURVEY
3.1 LITERATURE REVIEW
The application of artificial intelligence and computer vision in the beauty and fashion
industry has gained significant traction in recent years. Numerous studies and projects have 
explored the use of facial analysis for cosmetic recommendations, virtual try-on systems, and 
personal styling tools. This literature review examines existing technologies and
methodologies relevant to the development of a smart, face-shape-based Looksy: A Virtual 
hairstyle try-on.
1. Face Detection and Landmark Localization
Face detection is the foundational step for any facial analysis system. Traditional techniques 
like Haar Cascades and HOG + SVM classifiers provided a basis for early face detection 
models. However, these have largely been replaced by deep learning-based approaches, such
as convolutional neural networks (CNNs), due to their improved accuracy and robustness in 
varied lighting and orientation conditions.
MediaPipe, developed by Google, is widely used for real-time face mesh detection. It 
identifies 468 3D facial landmarks, enabling precise mapping of facial features. This data can 
be used to extract geometric measurements for face shape classification, as demonstrated in 
projects like "FaceShapeNet" (2019), which proposed a neural network-based approach to 
face shape recognition using landmark distances.
2. Face Shape Classification
Several research efforts have aimed to automate the classification of face shapes using 
landmark geometry and machine learning models. Some methods rely on calculating
distances between key facial points (e.g., forehead width, jawline length, cheekbone width) 
and applying rule-based logic. Others, such as the work by Ramya & Suresh (2020), 
introduced SVM and KNN classifiers trained on annotated facial datasets to predict the face 
shape with reasonable accuracy.
Despite these efforts, face shape classification remains a challenging problem due to 
overlapping characteristics and lack of standardized datasets. However, studies suggest that 
combining landmark ratios with machine learning improves classification precision and 
generalizability.
3. Emotion Detection and User Context
Emotion recognition can add an additional layer of personalization. The DeepFace
framework (developed by Facebook) and libraries like FER+ and AffectNet have 
demonstrated accurate emotion recognition capabilities using CNNs. Research shows that 
integrating emotion-based context in recommendation systems increases user engagement
and satisfaction, as explored in the 2021 study "Emotion-Aware Recommender Systems" by 
Gupta et al.
Table 1 Comparison with Other Platforms
S.no Name Link Features
1 Loreal www.loreal.com
 Automatically detects user’s face 
via webcam. Recommend hairstyle 
Accordingly(e.g., oval,round,square, 
Heart).
.
 Show trending hairstyle for man 
And women . Suggests styles 
based on face shape , age and 
Gender.
2 YouCam 
Makeup
www.youcammakeup.com  Use the live camera feature to
Apply makeup and accessories in 
Real time.
 It provides a platform for 
Experiment with a wide range of 
Makeup products and virtually try 
different hairstyles and hair colors 
to find your perfect look.
3 Looksy www.looksy.com
Real time face detection. 
Face Shape classification.
AI based Hairstyle
recommendation.
3.2 INFERENCES DRAWN
From the extensive research, implementation, and testing phases of the Looksy: A Virtual 
hairstyle try-on, several important inferences have been drawn:
1. Face Shape Significantly Influences Hairstyle Suitability
Through data analysis and expert insights, it was confirmed that different hairstyles 
complement specific face shapes. Proper identification of a user’s facial structure 
enables more accurate and aesthetically pleasing hairstyle suggestions.
2. Computer Vision Algorithms Are Effective for Facial Feature Analysis
Tools like MediaPipe and OpenCV proved to be highly effective in detecting facial 
landmarks with real-time accuracy. These technologies allowed precise mapping of 
facial proportions, which formed the backbone of the face shape classification 
module.
3. Emotion Detection Adds Personalization
Integrating emotion detection (using DeepFace) enhanced the system’s ability to 
personalize recommendations based on the user’s current mood, which may affect 
their style preferences. This added a human-like touch to the system’s responses.
4. Augmented Reality Increases User Engagement
Real-time AR previews of hairstyles significantly improved user experience. Users 
found it more intuitive and trustworthy to try on hairstyles virtually before making a 
decision, validating the inclusion of this feature in the final application.
5. Rule-Based and Machine Learning Approaches Complement Each Other
While rule-based systems worked well for initial face shape detection using geometric 
ratios, incorporating machine learning methods helped improve classification 
accuracy in ambiguous cases, especially when face shapes were not clearly defined.
6. Scalability Is Achievable with Modular Design
The modular architecture—separating frontend, backend, and AI processing—made 
the system scalable and easier to maintain. New hairstyles, face types, or 
recommendation rules can be added without impacting the overall functionality.
7. Practical Applications Extend Beyond Individual Users
The system shows great potential for deployment in salons, virtual beauty platforms, 
and e-commerce environments. Professionals can use it to offer data-driven 
consultations, enhancing customer satisfaction and service quality.
CHAPTER-4 
PROPOSED METHODOLOGY
4.1 CHALLENGES
Step 1: Capture face using webcam.
Step 2: Analyse face shape using Mediapipe. 
Step 3: Detect emotion using DeepFace.
Step 4: Fetch hairstyles suitable for shape and mood. 
Step 5: Overlay selected hairstyle.
Step 6: Voice assistant reads out current style.
Developing the Looksy: A Virtual hairstyle try-on posed several complex challenges across 
various technical domains. One of the primary difficulties was achieving accurate face shape 
detection from live webcam input. Variations in lighting, camera angles, facial expressions, 
and image resolution often affected the consistency of landmark detection. Extracting 
meaningful geometric features such as jawline width, cheekbone distance, and forehead span 
from these landmarks required precision, and even slight inaccuracies could result in 
misclassification of the face shape.
Another challenge involved classifying faces into clear shape categories. Many individuals 
exhibit facial features that lie between standard classifications like oval, round, or square, 
making it difficult to assign a definitive shape. This ambiguity necessitated the use of a 
combination of rule-based and machine learning approaches to improve accuracy and 
robustness. Additionally, integrating real-time augmented reality overlays introduced 
technical complexity, particularly in aligning hairstyles with a user’s head as it moved.
Ensuring smooth tracking and natural blending of virtual elements in live video streams 
demanded careful calibration and performance optimization.
Emotion detection, while enhancing personalization, presented its own set of problems. 
Facial expressions can be subtle or mixed, and capturing them accurately with pre-trained 
models required significant computational resources. Furthermore, the unavailability of 
comprehensive datasets linking hairstyles with face shapes and emotional context made data 
collection and annotation a labour-intensive task. Ensuring a responsive and intuitive user 
interface, capable of real-time video processing and dynamic recommendation display, also 
posed a challenge—especially on lower-end devices and mobile browsers. Integrating all
components seamlessly into a cohesive, user-friendly platform demanded thorough system 
testing, bug fixing, and performance tuning throughout the development lifecycle.
4.2 PROBLEM FORMULATION
The central problem addressed in this project is the lack of an intelligent and interactive
system that can recommend suitable hairstyles based on an individual's facial features and 
emotional state. Traditionally, people rely on generic beauty standards, hairstylist opinions, 
or trial and error to choose a hairstyle, which often leads to unsatisfactory results. There is no 
widely available tool that provides personalized hairstyle suggestions by analysing a user's 
actual face shape in real time. This gap highlights the need for a system that not only 
performs accurate facial analysis but also generates meaningful recommendations and 
visualizations tailored to the individual.
To formulate this problem technically, it is necessary to define a pipeline that begins with 
capturing the user’s facial data through a webcam. The system must then detect facial 
landmarks accurately, extract geometric features, and classify the face into predefined shapes 
such as oval, round, square, or heart. Based on this classification, and optionally the detected 
emotional expression, the system should recommend appropriate hairstyles from a curated 
database. Additionally, the application must allow users to virtually try on these hairstyles
using augmented reality overlays, making the recommendations not only informative but also 
interactive and visually verifiable.
This problem formulation involves multiple sub-problems including real-time facial 
landmark detection, face shape classification using algorithmic or machine learning methods, 
emotion recognition, database querying, and frontend AR rendering. The solution must 
integrate all these components into a unified platform that is accessible, fast, and easy to use. 
Addressing this problem has the potential to modernize the hairstyling experience, offering 
both individuals and professionals a smart and personalized tool for grooming and fashion 
decisions.
CHAPTER-5 
PROJECT WORK
Chapter-6 
REQUIREMENT
6.1 Hardware Requirements
 Webcam
 Minimum 4GB RAM
 i5 or higher CPU
6.2 Software Requirements
Operating System:
 Windows: Windows 7 or higher.
 Python 3.10+
 Flask
 HTML/CSS/JS
 OpenCV, Mediapipe, DeepFace
 Browser (Chrome recommended)
 User Face Capture
The system must allow users to capture real-time facial images using a webcam or 
upload a photo for analysis.
 Face Detection and Landmark Identification
The application must detect the user’s face and identify key facial landmarks using 
computer vision techniques (e.g., MediaPipe).
 Face Shape Classification
Based on the facial geometry, the system must classify the user's face into categories 
such as Oval, Round, Square, or Heart.
 Emotion Detection
The system should optionally detect the user's facial expression (e.g., Happy, Sad, 
Neutral) to enhance recommendations.
 Hairstyle Recommendation Engine
After face shape and emotion analysis, the system must recommend suitable 
hairstyles from the backend database.
 Virtual Try-On Feature
The application must allow users to see selected hairstyles overlaid on their face using 
CHAPTER-7 
CONCLUSION
The Looksy: A Virtual hairstyle try-on successfully demonstrates the practical application of 
artificial intelligence, computer vision, and web technologies to solve a real-world problem in 
the personal grooming and fashion industry. By leveraging facial landmark detection,
geometric analysis, and emotion recognition, the system offers users personalized hairstyle 
suggestions that suit their unique facial features and current mood. This intelligent approach 
addresses a common challenge faced by individuals—selecting a hairstyle that enhances their 
appearance and confidence—while also offering value to professionals in salons and virtual 
styling platforms.
The integration of real-time AR-based virtual try-on further enhances user experience, 
allowing individuals to visualize hairstyle options dynamically before making a choice. The 
modular architecture, combining Python (Flask) for backend processing and a responsive 
frontend, ensures scalability, maintainability, and potential for future enhancements.
Throughout the development process, challenges such as accurate face shape detection, real￾time video processing, and aesthetic overlay alignment were effectively addressed using 
state-of-the-art libraries like MediaPipe, OpenCV, and DeepFace. The project not only fulfils 
its objectives but also opens doors for broader applications in personalized fashion, e￾commerce, and interactive beauty consultations.
In conclusion, the system stands as a proof-of-concept for how intelligent recommendation 
engines can enhance everyday decision-making by combining data-driven analysis with user￾friendly interaction. With further refinement and integration of additional features, such as 
hairstyle filtering by gender or occasion, this project can be transformed into a full-fledged 
commercial solution.
7.1 FUTURE SCOPE
The Looksy: A Virtual hairstyle try-on lays a strong foundation for intelligent and 
personalized grooming assistance, and there are several promising directions for future 
development and enhancement:
1. Expansion of Hairstyle Database
The system can be extended by incorporating a larger, more diverse database of 
hairstyles categorized by gender, hair type, length, trends, and cultural preferences. 
This would allow for more inclusive and detailed recommendations tailored to a 
broader user base.
2. Integration with Hairstyle Trends and AI Personalization
Future versions could integrate APIs or datasets from fashion platforms to suggest 
trending hairstyles based on real-time data. Additionally, AI algorithms could be used 
to personalize suggestions based on user history, preferences, lifestyle, or even 
profession.
3. 3D Hairstyle Simulation
Implementing 3D hairstyle rendering using advanced graphics or deep learning-based 
generative models (e.g., GANs) could allow for more realistic and immersive virtual 
try-ons. This would improve the visual accuracy of how a hairstyle might actually 
look from different angles.
4. Mobile Application Development
Converting the system into a fully functional mobile application could make it more 
accessible to everyday users. With on-device processing and AR capabilities, the 
system could be used in salons, retail stores, or even during online shopping for hair 
products.
5. Voice and Gesture-Based Interaction
Enhancing the user interface with voice assistants and gesture control would improve 
usability, especially for users with accessibility needs or for hands-free operation 
during hairstyling sessions.
6. Integration with Salon Booking Systems
The platform could be connected to salon management software, allowing users to 
directly book appointments with recommended stylists or salons based on their chosen 
look, creating a seamless end-to-end experience.
7. Learning-Based Improvement and Feedback Loops
By incorporating user feedback after trying a recommended style (e.g., satisfaction 
rating, before-and-after images), the system can learn over time and refine its 
recommendation engine using supervised or reinforcement learning techniques.
In summary, the future scope of the project is vast and highly scalable. With continued 
development and refinement, this system has the potential to revolutionize the way 
individuals make grooming decisions and how professionals offer personalized beauty 
services.
REFERENCES
1. MediaPipe by Google. https://google.github.io/mediapipe/
2. OpenCV Documentation. https://docs.opencv.org/
3. DeepFace Library: A Lightweight Face Recognition and
Facial Attribute Analysis Framework. 
https://github.com/serengil/deepface
4. Fer2013 Dataset for Facial Emotion Recognition.
Available on Kaggle: 
https://www.kaggle.com/datasets/msambare/fer20
13
5. Flask - The Python Microframework. https://flask.palletsprojects.com/
6. HTML, CSS, and JavaScript Tutorials. Mozilla 
Developer Network (MDN). 
https://developer.mozilla.org/
7. Hairstyle Recommendations Based on Face Shapes – Industry
Studies & Blogs from beauty experts such as Allure and Vogue.
PROJECT SNAP
 Figure 1: Home page
Figure 2: Navigation bar
Figure 3: Trending hairstyles
Figure 4: How it works
Figure 5: Recommended products
Figure 6: Login
Figure 7: Registration
Figure 8: Profile section
Figure 9: Virtual try-on section
Figure 10 : virtual hairstyle sections , face analysis and current hairstyle
