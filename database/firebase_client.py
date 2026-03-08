import requests

FIREBASE_URL = os.getenv("FIREBASE_URL")


def get_collection(collection_name):

    url = f"{FIREBASE_URL}/{collection_name}.json"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None