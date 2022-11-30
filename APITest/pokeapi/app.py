from flask import Flask, render_template, request, redirect
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello():
    baseurl = 'https://pokeapi.co/api/v2'
    resource = 'pokemon'
    resource2 = 'pokemon-species'
    pokemon = 'rayquaza'
    url = f'{baseurl}/{resource}/{pokemon}'
    url2 = f'{baseurl}/{resource2}/{pokemon}'
    data = json.loads(requests.get(url).text)
    data2 = json.loads(requests.get(url2).text)
    
    sprite = data['sprites']['front_default']
    shiny_sprite = data['sprites']['front_shiny']
    name = data2['name']
    flavor_text  = data2['flavor_text_entries'][2]['flavor_text']
    pokedex = data2['pokedex_numbers'][0]['entry_number']
    types = []
    for t in data['types']:
        types.append(t['type']['name'])
    
    return render_template('index.html',sprite=sprite,shiny=shiny_sprite,name=name,flavor_text=flavor_text,pokedex=pokedex,
                           types=types)

if __name__ == '__main__':
    app.debug = True
    app.run()