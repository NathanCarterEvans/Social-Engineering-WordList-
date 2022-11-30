import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {"Accept-Language": "en-US, en;q=0.5"}
url = input("URL: ")
result = requests.get(url, headers=headers)

soup = BeautifulSoup(result.text, "html.parser")
print(soup.prettify())

#data storage
