import requests
import sys

#Afficher le document texte généré précédemment à partir de l'extraction des URLs de la page de résultats de la recherche sur Agorha
fichier = open("urls.txt",'r')
#Lire le contenu ligne par ligne dudit document
lignes = fichier.readlines()

#Télécharger les notices de la base

#Définir une liste des URLs à retenir : celles qui commencent par un "ark", et correspondent donc à une ressource documentaire.

#Convertir **par concaténation de chaînes de caractères** les liens d'accès à ces notices en **liens de téléchargement direct** de leurs données : ajouter le préfix du domaine Web de l'INHA, et l'extension de fichier (JSON-LD) à la place du nom de la base.
bonnes_lignes = ["https://agorha.inha.fr" + l.removesuffix("?database=88\n") + ".jsonld" for l in lignes if l.startswith("/ark:")]

#Assurer la continuité de la connexion à Agorha en tant que contributeurice
session = requests.session()
username = "anne.bugner-ext@bnf.fr"
password = "some_same_password"
login_data = {
    'tx_agorhaconnect_connect[userId]': username,
    'tx_agorhaconnect_connect[userPassword]': password,
    'tx_agorhaconnect_connect[__trustedProperties]': 'a:2:{s:6:"userId";i:1;s:12:"userPassword";i:1;}9868d9ebfac616839a376098c605d66ea848bab7' #variable indiquant toujours les cookies, pour se prémunir des déconnexions spontanées
}
session.post("https://agorha.inha.fr/login", data=login_data)

#Rassembler tous les fichiers JSON-LD en une liste '[]' au sein d'un seul élément '{}' racine

#Signaler l'ouverture de l'élément racine, et de la liste
print('{"base88":[') #identifiant de la base Agorha concernée

#(Noter que puisque la clé de cette élément est une chaîne de caractères, deux systèmes de guillemets doivent être employés pour ne pas causer de conflit avec ceux requis par la fonction print.)

#Vérifier le nombre de fichiers JSON-LD effectivement téléchargés par le script, pour comparer avec ce qu'Agorha annonçait, et la réponse HTTP de la requête
n = len(bonnes_lignes)
print(n, file=sys.stderr)

#Concaténer tous les fichiers JSON-LD téléchargés
for i in range(n):
    reponse = session.get(bonnes_lignes[i])

    #Afficher chaque notice ark captée dans notre liste
    print(reponse.text)

    # Apposer une virgule entre chacune d'elles, SAUF s'il s'agit de la dernière
    if i != n-1:
        print(",")

#Indiquer la clôture de la liste, et de l'élément racine
print("]}")
#Générer un document JSON-LD 'fichier_base' par la ligne de commande suivante: 'python filter_ark.py > fichier_base.jsonld'
