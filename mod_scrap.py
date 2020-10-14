import requests
from bs4 import BeautifulSoup
import lxml

#Creation de l'url
url="http://www.dataquest.io"

#Obtenir le contenu de la page
contenu = requests.get(url)
print(contenu)
html_contenu =contenu.text
print(html_contenu)
print("=" * 50)
#Conversion du contenu en element BeautifulSoup
soupe = BeautifulSoup(html_contenu,'lxml')
#Pret pour le parsing-recuperer les données d'interet à travers les balises
#Afficher le contenu de la balise title
print(soupe.title)
print("=" * 50)
print(soupe.title.text)
print("=" * 50)
#Afficher le texte présent dans tous les liens <a href=""> toto </a>
#fic = open("toto.txt", "a")
for adresse in soupe.find_all("a"):
    print(adresse.text)

#fic.close
