# covid data project

import requests
import json
import os
from datetime import datetime

def covid_data():

    url = "https://disease.sh/v3/covid-19/countries"

    res = requests.get(url)

    if res.status_code !=200:
        raise Exception(f"API Error: {res.status_code}")

    data = res.json()

    raw_data = "data/raw"
    os.makedirs(raw_data, exist_ok = True)

    timesstamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = (f"{raw_data}/covid_19_{timesstamp}.json")

    with open(file_path, "w") as csvfile:
        json.dump(data,csvfile)

    print(f"data saved to {file_path}")

if __name__ == "__main__":
    covid_data()

