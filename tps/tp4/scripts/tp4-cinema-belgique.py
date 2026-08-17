import os

from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://camille.ulb.be/"

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

headers = {
    "Cookie": os.environ["CAMILLE_COOKIE"]
}


# Interroger CAMille
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

# Afficher les informations sur le corpus
print("Recherche :", query)
print("Langue :", language)
print("Période :", year_from, "-", year_to)
print("Titre : Le Soir")


for text in soup.stripped_strings:
    if "résultats (" in text.lower():
        print(text)
        break


# Chercher le lien d'export XLSX
xlsx_url = None

for link in soup.find_all("a", href=True):
    text = link.get_text(" ", strip=True).lower()
    href = link["href"]

    if "xlsx" in text or "xlsx" in href.lower():
        xlsx_url = urljoin(BASE_URL, href)
        break


# Télécharger le fichier XLSX
if xlsx_url:
    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "camille_cinema_le_soir_1954_1955.xlsx"

    export = requests.get(
        xlsx_url,
        headers=headers,
        timeout=60,
    )

    export.raise_for_status()
    output_file.write_bytes(export.content)

    print("Export XLSX :", output_file)
else:
    print("Lien XLSX non trouvé.")