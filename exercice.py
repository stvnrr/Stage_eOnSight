import cv2
import numpy as np
import pandas as pd
import pytesseract
from pytesseract import Output
import json

# Charger l'image
image = cv2.imread('Genova.png')

# Passer l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Retirer les pixels qui ne sont pas assez blancs (le texte qu'on cherche est blanc)
mask = cv2.inRange(gray_image, 225, 255)
output = np.zeros_like(image)
output[mask == 255] = image[mask == 255]

# Inverser l'image pour avoir du texte noir sur fond blanc
output = cv2.bitwise_not(output)

# Appliquer la recherche de texte sur l'image
d = pytesseract.image_to_data(output, output_type=Output.DICT, lang='fra')
 
# Pour chaque texte trouver, filtrer ceux qui ont un niveau de confiance assez élevé et retirer les textes vides
# Créer le fichier JSON pour chaque texte trouvé
NbBox = len(d['level'])
s = []
for i in range(NbBox):
    conf = int(d['conf'][i])
    if conf > 50:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        text = d['text'][i].strip()
        if text.isalpha():
            print(text)
            element = {
                "text": text,
                "x": x,
                "y": y,
                "w": w,
                "h": h,
                "conf": conf,
            }
            s.append(element)

        # Afficher des rectangles sur les images
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


with open("output.json", "w") as outfile:
    json.dump(s, outfile, indent=4)
 
# Afficher les images avant et après traitement
cv2.imshow('output', output)
cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()