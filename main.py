import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
import numpy as np
from bs4 import BeautifulSoup
import requests

from utils import process_num_ratings, create_ds, write_to_file, handle_length

FILE_PATH = "db.txt"

def main():
    count = 0
    index = 1049000
    while True:
        URL = "https://www.imdb.com/title/tt" + "0" * (7 - len(str(index))) + str(index) + "/"

        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        try:
            storyline = soup.find("span", {"class": "sc-16ede01-1 kgphFu"}).text
            num_ratings = soup.find("div", {"class": "sc-7ab21ed2-3 dPVcnq"}).text
            rating = soup.find("span", {"class": "sc-7ab21ed2-1 jGRxWM"}).text
            title = soup.find("h1", {"class", "sc-b73cd867-0 eKrKux"}).text
            year = soup.find("a", {"class": "ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh"}).text

            list = soup.find("ul", {"class": "ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt"})
            try:
                length = list.findChildren("li")[2].text
            except IndexError:
                length = "error"    # Will become -1

            if storyline and rating and process_num_ratings(num_ratings) > 10000 and len(storyline) > 125 and len(year) == 4 and int(year) > 1945:
                print("")
                print(storyline)
                print(rating)
                print("")
                print(f"https://www.imdb.com/title/tt{'0' * (7 - len(str(index))) + str(index) + '/'}")
                count += 1

                write_to_file(rating, storyline, title, year, length, FILE_PATH)

            index += 1
        except AttributeError:
            index += 1

        if index % 25 == 0:
            print(f"Processing - {index}")



if __name__ == "__main__":
    main()