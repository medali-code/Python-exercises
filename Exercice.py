#"Quel age avez vous?"
# Si age en dessous de 10 ans => Vous avez (age) ans. Allez manger une barbe a papa"
# Si age entre 15 et 20 ans => Vous  avez (age) ans. Vous pouvez aller aux auto tamponneuses"
# Si age entre 25 et 60 ans => Vous  avez (age) ans. Vous pouvez faire le train fantome"
# Sinon => Je pense qu'il rentrer chez vous

age = int(input ("Quel age avez vous?"))
if age <10 :
    print(f"Vous avez {age} ans.Allez manger une barbe a papa")
elif age > 15  and age <20 : 
    print("Vous avez ",int(age), "ans, vous pouvez aller à l'auto-tamponnier.")
elif age > 25 and age <60 :
    print("Vous avez ",int(age), "ans, vous pouvez faire un trajet au train fantôme.")
else:
    print('Je pense qu il rentrer chez vous')