import os

import requests
from bs4 import BeautifulSoup


query = "cinema"
language = "fr-BE"
year_from = 1885
year_to = 1960

response = requests.get(
    "https://camille.ulb.be/",
    params={
        "query": query,
        "language": language,
        "year_from": year_from,
        "year_to": year_to,
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