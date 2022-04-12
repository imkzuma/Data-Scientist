import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/imkzuma/Data-Scientist/main/titanic/train.csv"

data = pd.read_csv(url)

lived = data[(data["Survived"] == 1)]
died = data[(data["Survived"] == 0)]

TempFemaleDied = died[(died["Sex"] == "female")]
TempMaleDied = died[(died["Sex"] == "male")]

TempFemaleSurvived = lived[(lived["Sex"] == "female")]
TempMaleSurvived = lived[(lived["Sex"] == "male")]

FemaleDied = len(TempFemaleDied)
FemaleSurvived = len(TempFemaleSurvived)

MaleDied = len(TempMaleDied)
MaleSurvived= len(TempMaleSurvived)


N = 1
R = np.arange(N)
width = 0.25

plt.bar(R, FemaleSurvived , color = "green" , width = width , edgecolor = "black" , label = "Perempuan Selamat")
plt.bar(R + width, FemaleDied , color = "blue" , width = width , edgecolor = "black" , label = "Perempuan Meninggal")

plt.bar(R + (width * 3), MaleSurvived , color = "red" , width = width , edgecolor = "black" , label = "Laki-Laki Selamat")
plt.bar(R + (width * 4), MaleDied , color = "purple" , width = width , edgecolor = "black" , label = "Laki - Laki Meninggal")

plt.ylabel("Jumlah Penumpang")
plt.xlabel("Perbandingan")

plt.xticks(R + width, [""])
plt.legend()
plt.title("Data Perbandingan Titanic")

plt.show()
