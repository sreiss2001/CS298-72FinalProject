import json
import requests
import random

def lambda_handler(event, context):
    
    ec2Req = requests.get('http://44.202.43.117:8080/').json()
    ran = random.randint(0, 10)  #generates a random number to pick a name
    name = ec2Req['results'][ran]['Name']  #locates only the name element

    #request to generate a praise for the random name picked
    req = requests.get("https://api.humorapi.com/praise?name=" + name + "&reason=you+did+amazing+this+semester&api-key=7e5d9d4dbb464dbfb0c429e560eae79c")
    req = req.json()
    
    print(req['text'])
    
    
    return {
        'statusCode': 200,
    }
