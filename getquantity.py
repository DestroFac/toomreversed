import requests
import json

# zuerst wird das Produkt hinzugefügt
add_to_cart_url = 'https://toom.de/shop/toomcheckout/pdp/add/'

add_to_cart_headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://toom.de/p/gewaechshaus-steffi-4-mm-hohlkammerplatten-aluminium-holzoptik-126-x-190-x-205-cm/4325164',
    'Origin': 'https://toom.de',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

add_to_cart_payload = {
    "articleId": "4325164",
    "quantity": 1,
    "marketId": "3766"
}

add_to_cart_cookies = {
    'PHPSESSID': '42a4935cae7ad1a4bbe26973c6a4e0f7',
    'market_id': '3766'
}

response_add_to_cart = requests.post(add_to_cart_url, headers=add_to_cart_headers, json=add_to_cart_payload, cookies=add_to_cart_cookies)



