Ratatouille =["Courgette","Aubergine","Poivron","Sel","Ail","Tomate"] 
#1  Listez les 2 premiers elements de la liste, et les 2 derniers.

#2  Trier par ordre les ingrédients

# 3  rajouter dans la liste le poivre

# 4 Ensuite dans la liste ci dessous recuperez 
# Le nombre 4 
# et aussi 4,8,et 3
# Juste le 3
# Et le 6
nombre = [1, [4, 8, 3], 5, [6], [[7]]]


Ratatouille =["Courgette","Aubergine","Poivron","Sel","Ail","Tomate"] 
# Listez les 2 premiers elements de la liste, et les 2 derniers.
print (Ratatouille [0:2])
print (Ratatouille [4:6])
# Trier par ordre les ingrédients
Ratatouille.sort()
print (Ratatouille)
# rajouter dans la liste le poivre
Ratatouille.append ("Poivre")
Ratatouille.pop (6)
print (Ratatouille)
# Ensuite dans la liste ci dessous recuperez 
# Le nombre 4 et aussi 4,8,et 3
# Juste le 3 et le 6
#nombre = [1, [4, 8, 3], 5, [6], [[7]]]
#print (nombre[1][0])  # 4
#print (nombre[1][0:3]) #4,8,et 3
#print (nombre[1][-1]) # Juste le 3
#print (nombre[-2][0]) # et le 6
