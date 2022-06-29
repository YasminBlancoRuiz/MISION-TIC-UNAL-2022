

import json
import requests
import peliculas


contenido=requests.get("https://raw.githubusercontent.com/erik-sytnyk/movies-list/master/db.json").text


db= json.loads(contenido)

with open("reto5.json", "w") as archivo:
    json.dump(db, archivo, indent=4)

resultado=peliculas.estadisticasDirector(db)
print(resultado)