import os
import requests
import pandas as pd
from dotenv import load_dotenv


# Chargement de la clé API depuis le fichier .env
load_dotenv()

API_KEY = os.getenv("EUROPEANA_API_KEY")

if not API_KEY:
    raise ValueError("La variable EUROPEANA_API_KEY est absente du fichier .env")


# Configuration de la recherche
API_URL = "https://api.europeana.eu/fulltext/search.json"
search_term = "journalisme belge"

headers = {
    "X-Api-Key": API_KEY
}

params = {
    "query": f'fulltext:"{search_term}"',
    "rows": 20,
    "profile": "rich"
}


# Appel de l'API
response = requests.get(
    API_URL,
    headers=headers,
    params=params
)

response.raise_for_status()

data = response.json()

print(f"Nombre total de résultats : {data['totalResults']}")


results = []

for item in data["items"]:
    title = item.get("title", [""])[0]
    creator = item.get("dcCreator", [""])[0]
    year = item.get("year", [""])[0]
    country = item.get("country", [""])[0]
    provider = item.get("dataProvider", [""])[0]
    link = item.get("guid", "")

    results.append([
        title,
        creator,
        year,
        country,
        provider,
        link
    ])


df = pd.DataFrame(
    results,
    columns=[
        "title",
        "creator",
        "year",
        "country",
        "provider",
        "link"
    ]
)

df