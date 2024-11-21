nombre = input("Entrez un nombre : ")
try :
    nombre = int(nombre) 
except : 
    print ("Désolé la valeur saisie n'est pas un nombre")    

try :
    Entier1 = int(input("Entrez un numérateur : "))
    Entier2 = int(input("Entrez un dénominateur : "))
    resultat = Entier1/Entier2
    print("Le résultat de la division est", resultat) 
except ValueError:
    print ("Désolé, les valeurs saisies ne sont pas des nombres.") 
except ZeroDivisionError:
    print ("Désolé, la division par zéro n'est pas permise")       
