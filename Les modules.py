# Les modules

# manipuler des nombres, gerer l'os, convertir des images, creer des sites webs

import random

a= random.randint(0,4)
print (a)

import random

a= random.uniform(0,1)
print (a)

import random

a= random.randrange(100)
print (a)

import random

a= random.randrange(0,1000,100)
print (a)

#.............

import os

chemin =""
dossier = os.path.join (chemin," Nouveau dossier ")
if not os.path.exists (dossier) :
    os.makedirs (dossier) #si cela nexiste pas donc creer moi un dossier
f = open('','')