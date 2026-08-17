import os

import requests
from bs4 import BeautifulSoup


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

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("Recherche :", query)

for text in soup.stripped_strings:
    if "résultats (" in text.lower():
        print(text)
        break