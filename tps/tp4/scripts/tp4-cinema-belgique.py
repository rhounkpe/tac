import os

import requests
from bs4 import BeautifulSoup


query = "cinema"
language = "fr-BE"
year_from = 1885
year_to = 1960

papers = {
    "JB427": "La Libre Belgique",
    "JB555": "L'Indépendance Belge",
    "JB567": "Journal de Bruxelles",
    "JB837": "Le Peuple",
    "JB1051": "Le Drapeau rouge",
    "BU1": "Annuaire Officiel de la presse belge",
    "JO3": "Journalistes 1979--2004",
}

params = [
    ("query", query),
    ("sortcrit", "relevance"),
    ("year_from", year_from),
    ("year_to", year_to),
    ("language", language),
]

for paper_id in papers:
    params.append(("paper", paper_id))

response = requests.get(
    "https://camille.ulb.be/",
    params=params,
    headers={
        "Cookie": os.environ["CAMILLE_COOKIE"]
    },
    timeout=30,
)

response.raise_for_status()
print("URL :", response.url)

soup = BeautifulSoup(response.text, "html.parser")

print("Recherche :", query)
print("Langue :", language)
print("Période :", year_from, "-", year_to)

print("Titres sélectionnés :")
for title in papers.values():
    print("-", title)


for text in soup.stripped_strings:
    if "résultats (" in text.lower():
        print(text)
        break