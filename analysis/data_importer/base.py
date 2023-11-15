import os
import json
import requests
from config import PROXIES

class BaseDataFetcher:

    INNER_SUBFOLDER = 'analysis/data-importer/data'

    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def get_data(self):
        current_directory = os.getcwd()
        subfolder_path = os.path.join(current_directory, self.INNER_SUBFOLDER)

        os.makedirs(subfolder_path, exist_ok=True)

        json_file_path = os.path.join(subfolder_path, self.filename)

        response = requests.get(self.url, proxies=PROXIES)

        if response.status_code == 200:
            data = response.json()

            with open(json_file_path, "w") as json_file:
                json.dump(data, json_file, indent=2)

            print(f"Data saved to {self.filename}")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)