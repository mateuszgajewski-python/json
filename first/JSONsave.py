import json

film =  {
        "title" : "Ale ja nie bede tego robil!",
        "release_year" : 1969,
        "won_oscar" : True,
        "actors": ("Arkadiusz Wlodarczyk", "Wiolleta Wlodarczyk"),
        "budget" : None,
        "credits" : {
                    "director" : "Arkadiusz Wlodarczyk",
                    "writer" : "Alan Burger",
                    "animator" : "Anime Animatrix"
                    }
        }

encodedFilm = json.dumps(film)

with open("sample.json", "w", encoding = "UTF-8") as file:
    json.dump(film, file, ensure_ascii = False)
