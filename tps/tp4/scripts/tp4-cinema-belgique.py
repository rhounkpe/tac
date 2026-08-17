import os

import requests
from bs4 import BeautifulSoup


query = "cinema"
language = "fr-BE"
year_from = 1954
year_to = 1955

paper = "JB838"  # Le Soir

params = {
    "query": query,
    "sortcrit": "relevance",
    "year_from": year_from,
    "year_to": year_to,
    "language": language,
    "paper": paper,
}

response = requests.get(
    "https://camille.ulb.be/",
    params=params,
    headers={
        "Cookie": os.environ["CAMILLE_COOKIE"]
    },
    timeout=30,
)

response.raise_for_status()


soup = BeautifulSoup(response.text, "html.parser")

print("Recherche :", query)
print("Langue :", language)
print("Période :", year_from, "-", year_to)


for text in soup.stripped_strings:
    if "résultats (" in text.lower():
        print(text)
        break