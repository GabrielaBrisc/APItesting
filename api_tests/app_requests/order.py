#inainte de order se face partea de authentification (api client)
from requests.structures import CaseInsensitiveDict
import requests


### Sumbit an order
# Allows you to submit a new order. Requires authentication.

# The request body needs to be in JSON format and include the following properties:

# bookId - Integer - Required
# customerName - String - Required

def  add_order(token, bookId, customerName):
    #caseinsensitivedict e de exemplu cand pun authorization in loc de Authorization
    headers1 = CaseInsensitiveDict()
    headers1["Accept"] = 'application/json'
    headers1["Authorization"] = f'Bearer {token}'
    json1 = {
        "bookId": bookId,
        "customerName": customerName
    }
    # pentru a plasa o comanda avem nevoie de acel token, de aceea,
    # cream o metoda care sa ne returneze care e tokenul (vezi api_client get_token method)
    response = requests.post(f"https://simple-books-api.glitch.me/orders", headers = headers1, json = json1)
    return response

def delete_order(token, orderId):
    headers = CaseInsensitiveDict()
    headers["Accept"] = 'application/json'
    headers["Authorization"] = f'Bearer {token}'
    response = requests.delete(f"https://simple-books-api.glitch.me/orders/{orderId}", headers=headers)
    return response

def get_orders(token):
    headers = CaseInsensitiveDict()
    headers["Accept"] = 'application/json'
    headers["Authorization"] = f'Bearer {token}'
    response = requests.get(f"https://simple-books-api.glitch.me/orders", headers=headers)
    return response

def get_order(token, orderId):
    headers = CaseInsensitiveDict()
    headers["Accept"] = 'application/json'
    headers["Authorization"] = f'Bearer {token}'
    response = requests.get(f"https://simple-books-api.glitch.me/orders/{orderId}", headers=headers)
    return response

def edit_order(token, bookId, customerName):
    headers = CaseInsensitiveDict()
    headers["Accept"] = 'application/json'
    headers["Authorization"] = f'Bearer {token}'
    json = {
        "bookId": bookId,
        "customerName": customerName
    }
    response = requests.get(f"https://simple-books-api.glitch.me/orders/{bookId}", headers=headers, json = json)
    return response