from urllib import response
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/imkzuma/Data-Scientist/main/mymovie-db/mymoviedb.csv"
data = pd.read_csv(url , lineterminator="\n")

def GetDownloadPoster(NameMovie):
    URL_DOWNLOAD = ""
    for index , row in data.iterrows():
        if NameMovie == row["Title"]:
            URL_DOWNLOAD = row["Poster_Url"]
    
    if URL_DOWNLOAD == "":
        print(f"{MovieName} tidak ada di database ini") 

    else:
        req = requests.get(URL_DOWNLOAD , allow_redirects = True)

        if req.ok:
            open(NameMovie + ".png" , "wb").write(req.content)
            print("Download Sukses")
        
        else: print(requests.exceptions.HTTPError)

df = pd.DataFrame(data)
data = data.filter(items=["Title" , "Genre" , "Popularity" , "Poster_Url"])

MovieName = input("Masukkan Nama Film: ")
GetDownloadPoster(MovieName)
