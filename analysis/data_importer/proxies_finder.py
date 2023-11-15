import requests
from bs4 import BeautifulSoup

valid = []
countries = []

def getProxies() -> list:
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text == 'elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies.append(proxy)
            countries.append(row.find_all('td')[3].text)
        else:
            pass
    print()
    print(f'Total of {len(proxies)} computed')
    print()
    return proxies

def extract(proxy, number):
    space = False
    try:
        r = requests.get('https://httpbin.org/ip', proxies={ 'http': proxy, 'https': proxy }, timeout=2)
        if r.status_code == 200:
            space = True
            valid.append(countries[number])
            working = {
                'proxy': proxy,
                'response': 'ok',
                'country': countries[number],
            }
        else:
            working = {
                'proxy': proxy,
                'response': 'error: status',
                'country': countries[number],
            }
    except requests.ReadTimeout as e:
        working = {
            'proxy': proxy,
            'response': 'error: timeout',
            'country': countries[number],
        }
        pass
    except requests.ConnectionError as e:
        working = {
            'proxy': proxy,
            'response': 'error: connection',
            'country': countries[number],
        }
        pass
    except requests.RequestException as e:
        working = {
            'proxy': proxy,
            'response': 'error: exception',
            'country': countries[number],
        }
        pass
    if space:
        print()
    print(working)
    if space:
        print()
    return proxy

def main():
    proxies = getProxies()

    for idx, p in enumerate(proxies):
        extract(p, idx)
    
    print()
    print()
    print(f'Total of {len(valid)/len(proxies)}% valid proxies from the following countries: {valid}')
    print()
    print()


main()
