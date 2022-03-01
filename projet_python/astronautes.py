import requests

# récup des infos sur le web
url = "http://api.open-notify.org/astros.json"
reponse = requests.get(url)

#
contenu = reponse.json()
print(contenu)

# alternative
texte = reponse.text
print(texte)
