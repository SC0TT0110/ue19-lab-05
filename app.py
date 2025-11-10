import requests

def prendre_blague():

    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        blague = response.json()
        print(f'{blague["setup"]}\n{blague["punchline"]}')
    else:
        print("erreur code http, impossible de récuperer une blague")

if __name__ == "__main__":
    prendre_blague()
