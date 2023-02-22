import requests
from bs4 import BeautifulSoup
import csv


baseUrl = 'https://www.studyrama.com'
uri = "/megamoteur/recherche?query=developpement&type=E%20F%20O"
response = requests.get(baseUrl + uri)



def getEndpoints(swoup):
    links = []

    ul = swoup.find("ul", {"class": "results"})
    lis = ul.findAll("li")
    for li in lis:
        a = li.find("a")
        links.append(baseUrl + a["href"])

    return links

def getInfoByPage(swoup):
    infosTriees = [swoup]
    return infosTriees

def swoup(url, process):
    response = requests.get(url)
    if response.ok:
        print("yes")
        soup = BeautifulSoup(response.text, 'html.parser')
        return process(soup)
    return []


def fileReader(file):
    result = []
    with open(file, 'r', encoding="UTF8", newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
           result.append(line) 
    return result

def fileWriter(file, fieldnames, data):
    with open(file, 'w', encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return fileReader(file)


data = fileReader("links.csv")

fields = ['test']
fileWriter('infos.csv', fields, data )

exit()

endpoints = swoup(baseUrl + uri,  getEndpoints)

# result = []
# for endpoint in endpoints:
#     result.extend(swoup(endpoint, getInfos))



# Initialisation des variables

# Definir la largeur(x) et la longueur de mon tableau
# a deux dimensions

# Creer une fonction qui me génère et renvoie un 
# tableau a deux dimension, rempli de cellules mortes
# ou vivantes 

# creer une fonction qui itere sur chaque cellule de
# mon tableau (ligne par ligne puis colonne par 
#  colonne)

# creer une fonction qui verifie les voisin d'une
# cellule

#definir une fonction prenant en parametre un tableau
# qui permet
#  d'Utiliser la fonction de verification dans la 
# fonction d'iteration du tableu
# et Renvoie une copie du tableau 


# Execution
# generer un tableau, l'assigner a une variable
# une boucle infinie (while True: ) 
# qui affiche le tablea de la fonction precedente 
# avec comme parametre le tableau, l'assigner a une variable "tableauCopy"
# definir que tableau est egal a tableau copy
