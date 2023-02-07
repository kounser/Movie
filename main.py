import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#data
movie = pd.read_csv("data/MovieData/IMDB-Movie-Data.csv")
#Average movie rating, number of directors
Am = movie["Rating"].mean()
nod = np.unique(movie["Director"]).shape[0]
##Distribution of ratings
plt.figure(figsize=(20, 8),dpi=100)
plt.hist(movie["Rating"].values, bins=20)
#add scale
max_ = movie["Rating"].max()
min_ = movie["Rating"].min()
t1 = np.linspace(min_, max_, num=21)
plt.xticks(t1)
plt.grid()
plt.show()
#Statistical classification of movies
temp_list = [i.split(",") for i in movie["Genre"]]
genre_list = np.unique([i for j in temp_list for i in j])
zeros = np.zeros([movie.shape[0],genre_list.shape[0]])
temp_movie = pd.DataFrame(zeros,columns=genre_list)
for i in range(1000):
    temp_movie.loc[i,temp_list[i]] = 1
genre = temp_movie.sum().sort_values(ascending=False)
genre.plot(kind="bar",figsize=(20, 8))
plt.show()



