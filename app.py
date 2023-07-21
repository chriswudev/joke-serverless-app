import requests
from db import add_records

JOKE_API_BASE_URL = "https://v2.jokeapi.dev/joke"

def fetch_jokes(params, context):
    category = params.get("category", "Any")
    language = params.get("language", "en")
    flag = params.get("flag")

    category = category or "Any"
    language = language or "en"

    url = f"{JOKE_API_BASE_URL}/{category}?lang={language}&type=single&amount=10"
    if flag:
        url += f"&blacklistFlags={flag}"

    try:
        response = requests.get(url)
        data = response.json()
        add_records(data["jokes"])
        return data
    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": str(e)
        }
