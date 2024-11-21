# La méthode split() sépare une chaine de caractères au niveau du séparateur
# spécifié et renvoie une liste de chaines de caractères.

text = "Python est un langage tres facile"
print (text.split(" "))

text = "1,2,3,4,5"
print (text.split(","))
text = "1#2#3#4#5"
print(text.split("#"))

text = "1 , 2, 3, 4, 5"
print (",".join (text.split(",")))

# La méthode startswith() prend trois paramètres:
# value(Obligatoire) : La valeur, pour vérifier si la chaine commence par celle-ci
# start(Optionnel) : Un entier spécifiant à quelle position démarrer la recherche
# end(Optionnel) : Un entier spécifiant à quelle position terminer la recherche   

str = "Bienvenue chez Moi"
res = str.startswith ("Bienvenue")
print (res)
res = str.startswith ("chez",10,14)
print (res)
res = str.endswith("chez")
print (res)

# Les methodes Is 

prenom = "mohamed"
print (prenom.islower())

prenom = "Mohamed"
print (prenom.islower())

prenom = "Mohamed Est Beau"
print (prenom.istitle())
prenom = "   "
print (prenom.isspace())

prenom = "50"
print (prenom.isdigit())

prenom = "mohamed50"
print (prenom.isalnum())
prenom = "mohamed50!"
print (prenom.isalnum())

# Comptez les caracteres et trouver une chaine

Cherche= "Amis du soir bonsoir"
print (Cherche.count("soir"))
print (Cherche.count(" soir"))
print (Cherche.find("soir"))
print (Cherche.index("soir"))
print (Cherche.find("jour"))

## 1er Exercice
phrase = "Bonjour tout le monde"
print (phrase.replace("Bonjour","bonsoir"))
## Script manquant

## 2eme Exercice
lettre_a_chercher ="T"
phrase = "tonton Toto , ton thé ta til oté ta toux ?"
print (phrase.count(lettre_a_chercher))

## 3eme Exercice Trier et resortez le resultat
chaine ="Alain, Bruno, Sandrine, Laurence, Brigitte"
chaine_split = chaine.split(",")
chaine_split.sort()
chaine_ordre=",".join(chaine_split)
print (chaine_split)