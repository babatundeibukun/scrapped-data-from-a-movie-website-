from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)
movies_page = response.text
soup = BeautifulSoup(movies_page, "html.parser")
title_list = [movies.get_text() for movies in soup.find_all(name="h3", class_="title")]
#to reverse the list
new_list=title_list[::-1]

with open("100 movies to watch.txt", "a") as movie_list:
    for movies in new_list:
        movie_list.write(f'{movies}\n')