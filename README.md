# Stage_eOnSight
Exercice pour le stage chez eOnSight

Voici mon rendu pour l'exercice d'OCR.
Il suffit de lancer le programme pour l'utiliser sur l'image Genova.png.

On obtient les résultats dans un ficher Json nommé output.json et on peut visualiser les rectangles des textes trouvées sur deux fenêtres qui montrent l'image avant et après traitement.

Mon approche pour résoudre cet exercice a été de remarquer que les textes recherchés étaient en blancs et donc de ne récupérer que le blanc sur les images pour pouvoir utiliser l'algorithme de recherche de texte sur des images plus simples à traiter par le programme.
