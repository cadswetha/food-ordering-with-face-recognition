from deepface import DeepFace
import os
from base64 import b64decode


# using deepface finding out the race of the person

def detectRace(image):
    header, encoded = image.split(",", 1)

    file_name = 'temp'
    savepath = "photos/"
    full_path1 = os.path.join(savepath, file_name+".jpg")
    # decoding and writing the encoded image in another .jpg file
    with open(full_path1, "wb") as f:
        f.write(b64decode(encoded))
    # only one attribute is required - race
    attributes = ['race']
    demography = DeepFace.analyze(full_path1, attributes)
    return demography['dominant_race']

# list of races - asian, indian, black,  white,   middle eastern ,  latino hispanic


# based on the race return a list of recommended cuisines

def recommendCuisine(raceInfo):
    if(raceInfo == 'asian'):
        return ['Japanese Cuisine', 'Chinese Cuisine', 'Thai Cuisine']
    if(raceInfo == 'indian'):
        return ['Indian Cuisine']
    if(raceInfo == 'black'):
        return ['Soul Food Cuisine']
    if(raceInfo == 'white'):
        return ['Italian Cuisine', 'American Cuisine']
    if(raceInfo == 'middle eastern'):
        return ['Labanese Cuisine', 'Arab Cuisine']
    if(raceInfo == 'latino hispanic'):
        return ['Italian Cuisine']
