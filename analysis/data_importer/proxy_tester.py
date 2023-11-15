import requests
from config import PROXIES

for proxy in PROXIES:
    try:
        print('Começando')
        response = requests.get('https://httpbin.org/ip', proxies=proxy)

        print(response)

        if response.status_code == 200:
            ip = response.json()['origin']
            print(f"IP Address: {ip}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except requests.ConnectionError:
        print('Broken proxy')
