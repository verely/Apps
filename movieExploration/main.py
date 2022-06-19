from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# retrieve top movie data from Internet Movie Database
response = requests.get(
    "https://www.imdb.com/chart/top/")
page = response.text

soup = BeautifulSoup(page, "html.parser")
data = soup.find_all(name="td", class_="titleColumn")

titles = []
years = []
ranks = []
# extract movie title, year and rank
for item in data:
    title = item.a.text
    year = re.sub("[()]", "", item.span.text)
    rank = (item.text.split('\n')[1]).strip()
    ranks.append(rank)
    titles.append(title)
    years.append(year)

# initialize data of lists.
data = {'Rank': ranks,
        'Title': titles,
        'Year': years
        }
# create DataFrame
movies_data = pd.DataFrame.from_dict({
    'Rank': ranks,
    'Title': titles,
    'Year': years
}).set_index('Rank')

# store data in csv
movies_data.to_csv("movies_data.csv")

# load data from csv
movies_data = pd.read_csv("movies_data.csv")

# explore data
top_movie_by_rank = movies_data["Title"].loc[movies_data['Rank'].idxmin()]
movie = movies_data.loc[movies_data['Year'].idxmin()]
oldest_movie = f'{movie["Title"]} {movie["Year"]}'
movie = movies_data.loc[movies_data['Year'].idxmax()]
newest_movie = f'{movie["Title"]} {movie["Year"]}'
print(f"Top movie: {top_movie_by_rank}")
print(f"Oldest movie: {oldest_movie}")
print(f"Newest movie: {newest_movie}")

movie_count_by_year = movies_data['Year'].value_counts().sort_index()
print(f"Movie count by year: {movie_count_by_year}")
