import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
import numpy as np
from bs4 import BeautifulSoup
import requests

from utils import *

FILE_PATH = "db.txt"

def main():
    count = 0
    index = 5
    while True:
        URL = "https://www.goodreads.com/book/show/" + str(index)
        rating = False
        ratings_count = False
        description = False
        title = False

        while count < 100:
            if count != 0 and count % 10 == 0:
                print(f"Count - {count}")
            try:
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")

                if not rating:
                    rating = soup.find("div", {"class": "RatingStatistics__rating"}).text
                    print(rating)
                
                if not ratings_count:
                    ratings_count = soup.find("span", {"data-testid": "ratingsCount"}).text
                    print(ratings_count)

                if not description:
                    description = soup.find("div", {"id": "descriptionContainer"}).findChildren("span" , recursive=True)[1].text
                    print(description)

                if not title:
                    title = soup.find("h1", {"id": "bookTitle"}).text.strip()
                    print(title)

                write_to_file(rating, ratings_count, description, title)

                print("")
                print(f"{title} - {URL}")
                print("")

                break
            except (AttributeError, IndexError):
                count += 1
                continue

        count = 0
        index += 1
        print(f"{index} - {URL}")


if __name__ == "__main__":
    main()