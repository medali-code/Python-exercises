liste =[1,2,3,4,5] #mutable #immutable
liste.append(6)
liste.extend ([7,8,9])
liste.remove(8)
nombre1 = liste[0]
print (liste)
print (nombre1) #indice

liste =[1,"olivier",False]

#index
Famille =["Antoine","Zoé","Sandrine","Patrick","Martine"]
classement= Famille.index("Patrick")
print (classement)

Famille =["Antoine","Zoé","Sandrine","Patrick","Martine"]
classement= Famille.count("Patrick")
print (classement)
Famille =["Antoine","Zoé","Sandrine","Patrick","Patrick","Martine"]
classement= Famille.count("Patrick")
print (classement)

Famille =["Antoine","Zoé","Sandrine","Patrick","Patrick","Martine"]
classement= Famille.sort()
print (Famille)
Famille =["Antoine","Zoé","Sandrine","Patrick","Patrick","Martine"]
classement= sorted(Famille)
print (classement)

Famille =["Antoine","Zoé","Sandrine","Patrick","Patrick","Martine"]
Famille.reverse()
print (Famille)

Famille =["Antoine","Zoé","Sandrine","Patrick","Patrick","Martine"]
classement= Famille.pop(3)
print (Famille)

Famille =["Antoine","Zoé","Sandrine","Patrick","Patrick","Martine"]
classement= Famille.clear()
print (Famille)
