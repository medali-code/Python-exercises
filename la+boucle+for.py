# les boucles vont repeter une opération un certain nbre de fois
# les boucles vont permettre de parcourir des iterables dont les listes font partie.
# Un itérable est un objet dont on peut parcourir les valeurs, 
# à l'aide d'un for par exemple. 
# Les boucles vont permettre de parcourir par exemple les fichiers 1 par 1
# sur votre disque dur. Ou soit les supprimer ou les renommer
# On va de cette facon laisser le script faire le job a notre place
# Il y a 2 boucles dans Python While et FOR
# for ressemble bcp a une structure conditionnelle

for i in [0,2,7,8,9]:
    print (i)
# on met i car c'est une convention que l'on retrouve souvent 
# donc la python va donner à i la valeur de l'itération courante.
# La on boucle sur les 5 itérations.
#1ere iteration i=0 et on part dans le PRINT
#2eme iteration i=1 et on part dans le PRINT etc...

# On peut aussi  boucler sur des chaines de caracteres
for lettres in "olivier":
    print (lettres)
#On peut aussi mettre en place la fonction range que l'on a vu precedement 

for i in range(8):
    print ("Olivier")

# En resume la boucle for permet de repeter une opération un certain nbre de fois
# ou aussi parcourir une structure de données (par exemple type de fichiers)
