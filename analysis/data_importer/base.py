import os
import json
import requests
from config import DATA_SUBFOLDER, PROXIES

class BaseDataFetcher:

    INNER_SUBFOLDER = DATA_SUBFOLDER

    def __init__(self, url, filename) -> None:
        if not url or not filename:
            raise ValueError("Both 'url' and 'filename' must be provided.")
        self.url = url
        self.filename = filename

    #def request(self) -> 'RequestWrapper':
    #    return self.RequestWrapper(self.url)

    def get_data(self) -> None:
        current_directory = os.getcwd()
        subfolder_path = os.path.join(current_directory, self.INNER_SUBFOLDER)

        os.makedirs(subfolder_path, exist_ok=True)

        json_file_path = os.path.join(subfolder_path, self.filename)

        response = requests.get(self.url, proxies=PROXIES[0])

        if response.status_code == 200:
            data = response.json()

            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file, indent=2)

            print(f"Data saved to {self.filename}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)


class RequestWrapper:

        def __init__(self, parent) -> None:
            self.parent = parent

        def get(self, url, headers=None, params=None, proxies=None) -> any:
            response = requests.get(self.url, headers=headers, params=params, proxies=proxies)
            return response.json()

        def post(self, url, headers=None, data=None, proxies=None) -> any:
            response = requests.post(self.url, headers=headers, data=data, proxies=proxies)
            return response.json()
