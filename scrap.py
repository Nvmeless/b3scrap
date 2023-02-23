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

def getInfoByPage(soup):
    fiches = []
    contacts = soup.find("div",{"class": "coordonnees"})
    if contacts is not None:
        tabs = contacts.findAll('li', {"class": "accordeon-item"})
        if tabs is not None:
            for contact in tabs:
                name = tryToCleanOrReturnBlank(contact.find("div", {"class": "accordeon-header"}))
                coord = contact.find("div", {"class": "accordeon-body"})
                adress = coord.find("p")
                tel = tryToCleanOrReturnBlank(coord.find("a", {"class": "tel"}))
                email = tryToCleanOrReturnBlank(coord.find("a", {"class": "email"}))
                title = tryToCleanOrReturnBlank(soup.find("title"))
                
                try:
                    adress = adress.getText()
                    cleanArrAdress = []
                    for ele in str(adress).split("\n"):
                        if ele != "":
                                cleanArrAdress.append(ele.strip())
                    
                    realAdress = cleanArrAdress[0]
                    realCC = cleanArrAdress[1]
                    realCountry = cleanArrAdress[2]
                except:
                    adress = ""
                    realAdress =""
                    realCC =""
                    realCountry =""
                    cleanArrAdress = []


                fiche = { 
                "name": name, 
                "adress": " ".join(cleanArrAdress),
                "realAdress": realAdress,
                "departement":realCC,
                "country": realCountry,
                "tel": tel,
                "email": email, 
                "title": title.replace(' - Studyrama', "")
                }
                fiches.append(fiche)
    return fiches 
def tryToCleanOrReturnBlank(str):
    try:
        result = str.getText().strip()
    except:
        result = ''
    return result
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



# fileWriter('infos.csv', fields, data)

endpoints = swoup(baseUrl + uri,  getEndpoints)

fields = ['lien']
rows = []
for endpoint in endpoints:
    row = {}
    row['lien'] = endpoint
    rows.append(row)
fileWriter('links.csv', fields, rows )

lignes = []
for link in fileReader('links.csv'):
    lignes.extend(swoup(link['lien'], getInfoByPage))

fields = ["name", "adress","realAdress","departement","country", "tel", "email", "title"]
fileWriter('infos.csv', fields, lignes )
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
