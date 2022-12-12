from flask import Flask
from flask import Flask,jsonify,request
from urllib.request import urlopen
import requests
import json
import random

app = Flask(__name__)

@app.route("/")
def names():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ran = random.randint(0, 25)  #generates a random number for picking a letter in the alphabet

    url = 'https://parseapi.back4app.com/classes/Listofnames_Names_Letter_' + letters[ran] + '?limit=10&keys=Name'

    #contains API keys
    headers = {
        'X-Parse-Application-Id': 'kmgrre2d52RDAlPH910iJqEaLILx04Xv9RkW6KmL', 
        'X-Parse-REST-API-Key': 'S8duwVKoL5kgi487kpFYwPZwBCCYScRlpv0LsFB7' 
    }

    data = json.loads(requests.get(url, headers=headers).content.decode('utf-8'))
    
    return json.dumps(data, indent=2)

if __name__ == '__main__':
     app.run (host="0.0.0.0", port=8080)
    
