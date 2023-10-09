import requests
import sys
from bs4 import BeautifulSoup

#Se connecter à Agorha en tant que contributeurice, pour viser les bases en cours d'alimentation, non seulement leurs notices publiques
def appel(url, username, password):
    session = requests.session()
    
    #Relier ensemble les variables du formulaire de connexion (extraites du code HTML source de la page) et les variables contenant nos identifiants personnels
    login_data = {
        'tx_agorhaconnect_connect[userId]': username,
        'tx_agorhaconnect_connect[userPassword]': password,
        'tx_agorhaconnect_connect[__trustedProperties]': 'a:2:{s:6:"userId";i:1;s:12:"userPassword";i:1;}9868d9ebfac616839a376098c605d66ea848bab7'  #Cette variable représente les cookies du site, qui doit être renseignée pour ne pas risquer d'être déconnecté.e de manière impromptue
    }
    #Remplir le formulaire de connexion
    session.post("https://agorha.inha.fr/login", data=login_data)

    #Recharger la page une fois la connexion effectuée
    response = session.get(url)

    #Afficher le code HTML source de la page du catalogue
    soupe = BeautifulSoup(response.text, 'html.parser')
    #Créer une liste vide qui réceptionnera les URLs que nous allons rechercher
    urls_tas = []

    #Rassembler les liens URL présents sur la page, renseignés par les éléments HTML <a>
    query_links = soupe.find_all("a")

    #Extraire les contenus des URLs, renseigné par l'attribut "href" de l'élément <a>, et les ajouter à notre liste
    for link in query_links:
        une_url = link.get('href')
        urls_tas.append(une_url)

    return urls_tas

# Déclarer les variables d'utilisation : URL source, username, password
#L'URL de la base, filtrée pour n'afficher que les notices de type "Oeuvre"
url_source_oeuvres = "https://agorha.inha.fr/recherche?terms=%2a&page=1&pageSize=1000&sort=&fieldSort=&noticeType=&type=simple&selectionId=&affichage=cartouche&facets=eyJub3RpY2VUeXBlIjp7ImZpbHRlcnMiOlsiQVJUV09SSyJdLCJmaWVsZCI6ImludGVybmFsLm5vdGljZVR5cGUiLCJmYWNldFNjb3BlIjoidGFiIiwiZmFjZXRPcmRlciI6MCwicGF0aEhpZXJhcmNoaWNhbCI6ZmFsc2V9LCJTdGF0dXRzIGRlcyBub3RpY2VzIjp7ImZpbHRlcnMiOltdLCJmaWVsZCI6ImludGVybmFsLnN0YXR1cyIsImZhY2V0U2NvcGUiOiJnZW5lcmFsIiwiZmFjZXRPcmRlciI6MSwicGF0aEhpZXJhcmNoaWNhbCI6ZmFsc2V9LCJEYXRlcyBkw6lidXQiOnsiZmlsdGVycyI6W10sImZpZWxkIjoiY29udGVudC5jb21wdXRlZEZhY2V0RGF0ZVN0YXJ0IiwiZmFjZXRTY29wZSI6ImdlbmVyYWwiLCJmYWNldE9yZGVyIjo1LCJwYXRoSGllcmFyY2hpY2FsIjp0cnVlfSwiRGF0ZXMgZmluIjp7ImZpbHRlcnMiOltdLCJmaWVsZCI6ImNvbnRlbnQuY29tcHV0ZWRGYWNldERhdGVFbmQiLCJmYWNldFNjb3BlIjoiZ2VuZXJhbCIsImZhY2V0T3JkZXIiOjYsInBhdGhIaWVyYXJjaGljYWwiOnRydWV9LCJQZXJzb25uZXMiOnsiZmlsdGVycyI6W10sImZpZWxkIjoiY29udGVudC5jb21wdXRlZEZhY2V0UGVyc29uIiwiZmFjZXRTY29wZSI6ImdlbmVyYWwiLCJmYWNldE9yZGVyIjo0LCJwYXRoSGllcmFyY2hpY2FsIjp0cnVlfSwiTGlldXgiOnsiZmlsdGVycyI6W10sImZpZWxkIjoiY29udGVudC5jb21wdXRlZEZhY2V0UGxhY2UiLCJmYWNldFNjb3BlIjoiZ2VuZXJhbCIsImZhY2V0T3JkZXIiOjcsInBhdGhIaWVyYXJjaGljYWwiOnRydWV9LCJEb2N1bWVudHMgYXNzb2Npw6lzIjp7ImZpbHRlcnMiOltdLCJmaWVsZCI6ImNvbnRlbnQuY29tcHV0ZWRGYWNldEF0dGFjaG1lbnQiLCJmYWNldFNjb3BlIjoiZ2VuZXJhbCIsImZhY2V0T3JkZXIiOjIsInBhdGhIaWVyYXJjaGljYWwiOmZhbHNlfSwiQmFzZXMgZGUgZG9ubsOpZXMiOnsiZmlsdGVycyI6WyJMYSBmYWJyaXF1ZSBtYXTDqXJpZWxsZSBkdSB2aXN1ZWwuIFBhbm5lYXV4IHBlaW50cyBlbiBNw6lkaXRlcnJhbsOpZSBYSUlJZS1YVkllIHNpw6hjbGVzIl0sImZpZWxkIjoiY29udGVudC5yZWNvcmRNYW5hZ2VtZW50SW5mb3JtYXRpb24uZGF0YWJhc2VMYWJlbC52YWx1ZSIsImZhY2V0U2NvcGUiOiJnZW5lcmFsIiwiZmFjZXRPcmRlciI6MywicGF0aEhpZXJhcmNoaWNhbCI6ZmFsc2V9fQ%3D%3D&filters=&withAttachment=false"
#Ou, si souhaité, l'URL de la base en général
url_source = "https://agorha.inha.fr/recherche?page=1&pageSize=1000&terms=%2a&facets=eyJCYXNlcyBkZSBkb25uXHUwMGU5ZXMiOnsiZmlsdGVycyI6WyJMYSBmYWJyaXF1ZSBtYXRcdTAwZTlyaWVsbGUgZHUgdmlzdWVsLiBQYW5uZWF1eCBwZWludHMgZW4gTVx1MDBlOWRpdGVycmFuXHUwMGU5ZSBYSUlJZS1YVkllIHNpXHUwMGU4Y2xlcyJdLCJmaWVsZCI6ImNvbnRlbnQucmVjb3JkTWFuYWdlbWVudEluZm9ybWF0aW9uLmRhdGFiYXNlTGFiZWwudmFsdWUiLCJwYXRoSGllcmFyY2hpY2FsIjpmYWxzZSwiZmFjZXRPcmRlciI6MywiZmFjZXRTY29wZSI6ImdlbmVyYWwifX0%3D"
username = "anne.bugner-ext@bnf.fr"
password = "some_passeword"

# Obtenir un premier jet de nos URLs :
nos_urls = appel(url_source_oeuvres, username, password)

# En afficher les URLs une par une, afin que 1 URL occupe 1 ligne dans le document créé par le script.
for url in nos_urls:
    print(url)

#Pour que le script génère un document texte, du nom de 'urls.txt', exécuter la commande 'python html_urls.py > urls.txt'
