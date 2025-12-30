from requests import Request, Response
from api_decorator import get
import json


base_url = "https://pokeapi.co/api/v2/"

@get(f"{base_url}pokemon/")
def get_pokemon(request: Request, response: Response, param: str):
    return response, request

@get(f"{base_url}pokemon-species/")
def get_pokemons(request: Request, response: Response):
    return response, request

@get(f"{base_url}pokemon-species/")
def get_pokemons_paginated(request: Request, response: Response, query_params: str):
    return response, request
    

response, request = get_pokemons()
print("URL:", request["url"])
print("Method:", request["method"])
print("Status:", response.status_code)
print("data:", json.dumps(response.json(), indent=4, ensure_ascii=False))
print("Total Pokemons:", response.json().get("count"))

response2, request2 = get_pokemon(param="pikachu")
print("URL:", request2["url"])
print("Method:", request2["method"])
print("Status:", response2.status_code)
# print("data:", json.dumps(response2.json(), indent=4, ensure_ascii=False))
print("Name:", response2.json().get("species"))

response, request = get_pokemons_paginated(query_params={"offset": 0, "limit": 5})
print("URL:", request["url"])
print("Method:", request["method"])
print("Status:", response.status_code)
print("data:", json.dumps(response.json(), indent=4, ensure_ascii=False))
print("Total Pokemons:", response.json().get("count"))
print("Total Pokemons in page:", len(response.json().get("results")))
