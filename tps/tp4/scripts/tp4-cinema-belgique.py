import os

import requests
from bs4 import BeautifulSoup


query = "cinema"
language = "fr-BE"

response = requests.get(
    "https://camille.ulb.be/",
    params={
        "query": query,
        "language": language,
    },
    headers={
        "Cookie": os.environ["CAMILLE_COOKIE"]
    },
    timeout=30,
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("Recherche :", query)
print("Langue :", language)

for text in soup.stripped_strings:
    if "résultats (" in text.lower():
        print(text)
        break