import requests
import json

url = "https://api.toom.de/public/api/markets"
response = requests.get(url)
data = json.loads(response.text)

if 'markets' in data:
    markets = []
    for market in data['markets']:
        market_info = {
            'id': market.get('id', ''),
            'name': market.get('name', ''),
            'phone': market.get('phone', ''),
            'email': market.get('email', ''),
            'pickupEmail': market.get('pickupEmail', '')
        }
        markets.append(market_info)

    with open('markets.json', 'w', encoding='utf-8') as f:
        json.dump(markets, f, ensure_ascii=False, indent=4, separators=(',', ': '))
        for market in markets:
            if 'pickupEmail' in market:
                f.write("\n") # Zeilenumbruch hinzufügen, wenn das Feld 'pickupEmail' vorhanden ist
else:
    print("Error: 'markets' field not found in JSON response")
