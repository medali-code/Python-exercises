note= int(input("Quel note avez vous ?"))
moyenne =10
Max =20

if  note < 3 :
    print (f"Vous avez eu {note}.Dommage il vous manquait {moyenne - note} points pour avoir la moyenne c'est sans commentaire...") 
if  note >3 and note< 6 :
    print (f"Vous avez eu {note}.Dommage il vous manquait {moyenne - note} points pour avoir la moyenne Il faut tout revoir...") 
if  note >6 and note< 9  :
    print (f"Vous avez eu {note}.Dommage il vous manquait {moyenne - note} points pour avoir la moyenne peut mieux faire...") 
if  note ==10 :
    print (f"Vous avez tout juste la moyenne") 
if  note >11 and note< 14  :
    print (f"Vous avez eu {note}.Dommage il vous manquait {Max - note} points pour avoir la note maximale,c'est satisfaisant") 
if  note >14 and note <20  :
    print (f"Vous avez eu {note}.Dommage il vous manquait {Max - note} points pour avoir la note maximale, c'est une tres bonne note") 
if  note ==20 :
     print (f"We are the champions my friend") 