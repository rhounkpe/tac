import os

import requests


query = "cinema"

response = requests.get(
    "https://camille.ulb.be/",
    params={
        "query": query,
    },
    headers={
        "Cookie": os.environ["CAMILLE_COOKIE"]
    },
    timeout=30,
)

print("Recherche :", query)
print("Status :", response.status_code)
print("URL :", response.url)
print("Taille de la réponse :", len(response.text), "caractères")