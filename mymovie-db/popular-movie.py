#Popular movie Graph based on popularity

import pandas as pd 
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/imkzuma/Data-Scientist/main/mymovie-db/mymoviedb.csv"
data = pd.read_csv(url , lineterminator = "\n")

Name = []
Popular = []

for index , row in data.iterrows():
    Name.append(row["Title"])
    Popular.append(row["Popularity"])

    if index == 4: break

plt.bar(Name , Popular)
plt.title("Top 5 Popular Movie This Year")

plt.ylabel("Popularity")
plt.show()
