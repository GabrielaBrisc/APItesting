# POST /api-clients/

from random import randint
import requests

def login(clientName=None, clientEmail=None):
    body ={
        'clientName': clientName,
        'clientEmail': clientEmail
    }
    #apelam api ul, iar in test api client testam partea de login
    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json = body)
    return response

#pentru a plasa o comanda avem nevoie de acel token, de aceea, cream o metoda care sa ne returneze care e tokenul (vezi order)

def get_token():
    nr =randint(1, 99999)
    json = {
        'clientName': "Gabi",
        'clientEmail': f'valid_email_test{nr}@mail.com'
    }
    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json = json)
    return response.json()['accessToken']


