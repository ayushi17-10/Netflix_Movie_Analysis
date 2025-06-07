years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

movie_dict = {"years": years, "durations": durations}

movie_dict

from matplotlib import pyplot as plt
import pandas as pd

durations_df = pd.DataFrame(movie_dict)

print(durations_df)

import pandas as pd

durations_df = pd.DataFrame(movie_dict)

print(durations_df)

netflix_df = pd.read_csv("netflix_data.csv")

netflix_df.head(2)

netflix_df.info()

netflix_df_movies_only = netflix_df[netflix_df["type"]== "Movie"]

netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]

netflix_movies_col_subset.head()

fig = plt.figure(figsize=(12,8))

plt.scatter(netflix_movies_col_subset["release_year"],
           netflix_movies_col_subset["duration"])

plt.title("Movie Duration by Year of Release")

plt.show()

short_movies = netflix_movies_col_subset.query("duration < 60")

short_movies.head(20)

colors = []

for lab, row in netflix_movies_col_subset.iterrows():
    if row["genre"] == "Children":
        colors.append("red")
    elif row["genre"]== "Documentaries":
        colors.append("blue")
    elif row["genre"]== "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")
            
colors[:10]

plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

plt.scatter(netflix_movies_col_subset["release_year"],
           netflix_movies_col_subset["duration"],
           color= colors)

plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie duration by year of release")

plt.show()

are_movies_getting_shorter = "No"
print(are_movies_getting_shorter)