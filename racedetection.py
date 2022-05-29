from deepface import DeepFace
import os
from base64 import b64decode


def detectRace(image):
    header, encoded = image.split(",", 1)
    file_name = 'temp'
    savepath = "photos/"
    full_path1 = os.path.join(savepath, file_name+".jpg")
    with open(full_path1, "wb") as f:
        f.write(b64decode(encoded))
    attributes = ['race']
    demography = DeepFace.analyze(full_path1, attributes)
    return demography['dominant_race']

# asian indian black  white   middle eastern   latino hispanic


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
