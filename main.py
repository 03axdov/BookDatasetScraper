import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
import numpy as np
from bs4 import BeautifulSoup
import requests

from utils import *


count = 0
index = 135852
while count < 5:
    URL = "https://www.imdb.com/title/tt" + "0" * (7 - len(str(index))) + str(index) + "/"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        storyline = soup.find("span", {"class": "sc-16ede01-1 kgphFu"})
        num_ratings = soup.find("div", {"class": "sc-7ab21ed2-3 dPVcnq"})
        rating = soup.find("span", {"class": "sc-7ab21ed2-1 jGRxWM"})
        if storyline.text and rating.text and process_num_ratings(num_ratings.text) > 10000:
            print("")
            print(storyline.text)
            print(rating.text)
            print("")
            print(f"https://www.imdb.com/title/tt{'0' * (7 - len(str(index))) + str(index) + '/'}")
            count += 1
        index += 1
    except AttributeError:
        index += 1