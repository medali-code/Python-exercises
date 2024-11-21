Arretdutrain = "o"
while Arretdutrain == "o":
    print("On continue jusqu'a la prochaine station !")
    input("Voulez-vous arreter le train ? o/n ")
   

 


Arretdutrain = "o"
while Arretdutrain == "o":
    Arretdutrain=input("Voulez-vous arreter le train ? o/n ")
    if Arretdutrain =="n":
       print("On continue jusqu'a la prochaine station !")
    if Arretdutrain =="o":
        print("On descend a cette station!")
        break