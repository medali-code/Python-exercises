# Len permet de recuperer la longueur de la chaine de caractere
longueur = len ("Olivier23")
print (longueur)
# par contre pour la liste cela retourne le nbre delements 
liste = len(["A","B","C"])
print (liste)
# round permet d'arrondir au nbre le + proche
nombre=round(1.9)
print (nombre)
# min et max permet de recuperer la valeur minimum et la valeur maximum a l'interieur
# dune structure de donnée
valeur=min([10,25,92,87,101,3])
print (valeur)
# Sum recupere le total d'une opération
valeur=sum([20+20+40+1876])
print (valeur)
# Range permet de créer une liste de nombre
valeur=range(5)
valeur=list(valeur)
print (valeur)
# Avec Python 3, la fonction range 
# ne retourne pas directement une liste, mais un objet de type range
# Si vous souhaitez récupérer cet objet range sous la forme d'une liste, 
# il suffit de le convertir avec la fonction list :