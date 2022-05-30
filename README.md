# Food ordering with face recognition

## Microsoft-Engage-Project

Food ordering and recommendation system using face_recognition and DeepFace

This is a web based facial login/sign-up device that makes food ordering process easier and it makes use of Flask server. It also has the provision for registering face for new entries.

#### It also recommends the most preferred cuisines based on the person's racial identity

### Preview

### Tools & Libraries Used

- Python - face_recognition - https://github.com/ageitgey/face_recognition
- Python - pickle
- Python - DeepFace - (For recommendation part)

### Working

1. clone the entire repository

   - Before installing any of the requiremretns, make sure that Microsoft Visual Studio and CMake is already installed
   - Please refer this :https://github.com/ageitgey/face_recognition/issues/175

2. Install all the requirements from the requirements.txt file
3. Before running the application we will have to download the weights(deepface) by clicking on the link : https://github.com/serengil/deepface_models/releases/download/v1.0/race_model_single_batch.h5
4. After the above file gets downloaded, paste it in the 'weights' folder of .deepface (present in C:\Users\ _user_name_ )
5. Now run python servery.py
6. Go to browser and type localhost:5000 to access the site
