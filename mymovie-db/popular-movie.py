#Popular movie Graph based on popularity

import pandas as pd 
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/imkzuma/Data-Scientist/main/mymovie-db/mymoviedb.csv"
data = pd.read_csv(url , lineterminator = "\n")

def ShowGraph(Name , Popular):
    for index in range(5):
        plt.bar(Name[index] , Popular[index] , label = str(index + 1) + " " + Name[index] + " = " + str(Popular[index])) 

    plt.title("Top 5 Popular Movie This Year")
    plt.legend()

    plt.ylabel("Popularity")
    plt.show()

data = data.sort_values(["Popularity"] , ascending = False)
data = data.filter(items = ["Title" , "Popularity"])

print(data.head(5))

Name = []
Popular = []

for index , row in data.iterrows():
    Name.append(row["Title"])
    Popular.append(row["Popularity"])

    if index == 4: break

ShowGraph(Name , Popular)
