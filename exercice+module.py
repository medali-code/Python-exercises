import random

prix1 = random.randint(0, 10)
prix2 = random.randint(0, 10)
print (prix1)
print (prix2) 
if prix1 > prix2:
    print("Le prix1 est plus grand que le prix 2 ")
elif prix1 < prix2:
    print("Le prix2 est plus grand que le prix 1")
elif prix1 == prix2:
    print("Les prix1 et les prix2 sont égaux")


