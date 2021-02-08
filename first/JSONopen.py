import json

encodedMovie = ('{"title": "Ale ja nie bede tego robil!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Wlodarczyk", "Wiolleta Wlodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Wlodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}')


decodedMovie = json.loads(encodedMovie)

with open("sample.json", encoding = "UTF-8") as file:
    wynik = json.load(file)
