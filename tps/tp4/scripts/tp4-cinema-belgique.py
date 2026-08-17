import os
import requests

response = requests.get(
    "https://camille.ulb.be/?page=about",
    headers={
        "Cookie": os.environ["CAMILLE_COOKIE"]
    },
    allow_redirects=False,
    timeout=30,
)

print("Status :", response.status_code)
print("Location :", response.headers.get("Location"))