mdp = input("Entrez un mot de passe (min 6 caractères et max 10 caracteres) : ")
mdp_moinsde6 = "votre mot de passe est trop court."
mdp_plusde10 = "votre mot de passe est trop long"

if  len(mdp) < 6 :
    print(mdp_moinsde6)
elif len(mdp) > 10 :
    print(mdp_plusde10)
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Votre inscription est terminée.")