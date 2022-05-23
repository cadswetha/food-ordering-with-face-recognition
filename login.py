from base64 import b64decode
import face_recognition as fr
import time
import os
import pickle
from PIL import Image
import numpy as np


def login_check(email, image):
    face_match = 0
    header, encoded = image.split(",", 1)
    # jpg file name for live photo
    file_new = str(time.time_ns())
    # jpg file name  for registered photo
    file_exist = str(time.time_ns()+1)

    try:
        # local system path for storing the images
        # ******change it afterwards*****
        savepath = "C:/Users/sweth/OneDrive/Desktop/facerecog/MS_Project_Copy/Microsoft-Engage-Project/photos/"

        # photo1
        full_path1 = os.path.join(savepath, file_new+".jpg")

        # loading the file by decoding the 'encoded image'
        with open(full_path1, "wb") as f:
            f.write(b64decode(encoded))

        # photo2
        full_path2 = os.path.join(savepath, file_exist+".jpg")

        # loading the pickel file
        data = pickle.loads(open("data.pickle", "rb").read())

        # loading the file with data stored while registering
        with open(full_path2, "wb") as f:
            f.write(b64decode(data[email]))

        try:

            got_image = fr.load_image_file(full_path1)

            existing_image = fr.load_image_file(full_path2)

            got_image_facialfeatures = fr.face_encodings(got_image)[0]

            existing_image_facialfeatures = fr.face_encodings(existing_image)[
                0]

            # comparing the faces
            results = fr.compare_faces(
                [existing_image_facialfeatures], got_image_facialfeatures, tolerance=0.4)

            if(results[0]):
                return "Successfully Logged in!"

            else:
                return "Failed to Log in!"

        except Exception as e:
            print(e.__cause__)
            return "Image not clear! Please try again!"

    except Exception as e:
        print(e.__cause__)
        return "Data does not exist!"
