import requests
import matplotlib.pyplot as plt
from PIL import Image
import urllib.request
import numpy as np

pokemon = input("introduce el nombre de un pokemon: ")
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
res = requests.get(url)

if res.status_code != 200:
    print("no se ha encontrado ningun pokemon")
    exit()

with urllib.request.urlopen(res.json()['sprites']['front_default']) as url:
    imagen = np.array(Image.open(url))
    
plt.title(res.json()['name'])
impgplot = plt.imshow(imagen)
plt.show()