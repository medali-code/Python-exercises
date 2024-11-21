# Ne modifiez pas les variables ci-dessous
protocole = "http://"
nom_du_site = "eloa"
extension = "fr"
# Modifiez le code à partir d'ici 
URL = f"{protocole}www.{nom_du_site}.{extension}"
URL2= "{}www.{}.{}".format(protocole,nom_du_site,extension)

print (URL)
print (URL2)


