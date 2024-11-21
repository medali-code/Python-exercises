# Rappel sur les méthodes et les fonctions
# Une méthode c'est une fonction qui appartient a un objet

#liste = [5,3,2,8,9]
#sorted(liste)
#print (liste)
# Ce n'est pas trié car elle va retourner une version ordonné de la liste
# mais sans touché a la liste dorigine, il faut ecraser cette liste par la fonction sorted

#liste = [5,3,2,8,9]
#liste= sorted(liste) #sorted nous reaffecte la liste retourné a la variable liste
#print (liste)

liste = [5,3,2,8,9]
liste.sort () #la méthode est associée a une liste sans faire de reaffectation
print (liste)

# Erreur courante 
liste = [5,3,2,8,9]
liste=liste.sort () #Renvoie None donc rien
print (liste)
# la méthode est déja appliquée et on reaffecte le resultat dans la liste dorigine
# contrairement a la fonction sorted, la methode sort ne retourne rien d'ou NONE
