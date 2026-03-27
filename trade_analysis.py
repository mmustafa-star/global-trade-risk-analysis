import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Year":[2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
    "Oil_Price":[52,43,50,65,60,39,70,100,85,82],
    "Risk_Level":[2,2,2,3,3,5,4,5,4,3]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["Oil_Price"], marker='o')

plt.title("Oil Price vs Global Risk")
plt.xlabel("Year")
plt.ylabel("Oil Price")
plt.grid()

plt.show()
