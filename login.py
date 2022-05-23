from base64 import b64decode
from typing import final
import face_recognition as fr
import time
import os
import pickle

from numpy import full


def login_check(email, image):
    face_match = 0
    header, encoded = image.split(",", 1)
    file_new = str(time.time_ns())
    file_exist = str(time.time_ns())
    try:
        savepath = "C:/Users/sweth/OneDrive/Desktop/facerecog/MS_Project_Copy/photos/"
        full_path1 = os.path.join(savepath, file_new+".png")
        with open(full_path1, "wb") as f:
            f.write(b64decode(encoded))

        full_path2 = os.path.join(savepath, file_exist+".png")
        data = pickle.loads(open("data.pickle", "rb").read())
        with open(full_path2, "wb") as f:
            f.write(b64decode(data[email]))

        try:
            got_image = fr.load_image_file(full_path1)
            existing_image = fr.load_image_file(full_path2)
        except Exception as e:
            print(e.__cause__)
            return "Image not clear! Please try again!"
        got_image_facialfeatures = fr.face_encodings(got_image)[0]
        existing_image_facialfeatures = fr.face_encodings(existing_image)[0]
        results = fr.compare_faces(
            [existing_image_facialfeatures], got_image_facialfeatures)
        if(results[0]):
            return "Successfully Logged in!"
        else:
            return "Failed to Log in!"
    except Exception as e:
        print(e.__cause__)
        return "Data does not exist!"
