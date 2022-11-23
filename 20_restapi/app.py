#Twitter: Brian Wang (Donald Bi)
#SoftDev
#K20 -- REST API
#2022-11-21
#time spent: .7 hr

from flask import Flask, render_template, request, session, redirect
import requests
import json

app = Flask(__name__)
with open('key_nasa.txt') as f:
    key = f.readline()


@app.route('/', methods=['GET', 'POST'])
def hello():
    print("what")
    jason = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}').json()
    #dict = json.load(jason)
    #jason = request.get_json('https://api.nasa.gov/planetary/apod?api_key=V3ZJOBoMLH0nhHXIue2Vbmabs8gRfMp4alnPqzOY')
    print("hi")
    print(jason)
    #dict = json.loads(jason)
    return render_template("main.html", url = jason["url"]) 
    
if __name__ == "__main__":
    app.debug = True
    app.run() 