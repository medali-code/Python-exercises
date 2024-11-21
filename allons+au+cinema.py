a= b = "" # declarez 2 variables vides
while not  (a.isdigit() and b.isdigit()) : # tant que je n'ai pas de nombre je boucle
    a =input ("Entrez un prix de votre premier ticket : ")# 1er input
    b =input ("Entrez un prix de votre deuxieme ticket: ")# 2eme input
    if not (a.isdigit and b.isdigit()): # si pas ne nombre on sort le print
        print ("Veuillez entrer un nombre valide")

print (f"Le resultat du prix de vos 2 tickets sont de {int(a) +  int(b)} euros ")