#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

Eu = ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland",
      "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg",
      "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovak Republic", "Slovenia", "Spain", "Sweden"]

G20 = ["Argentina", "Australia", "Brazil", "Canada", "China", "France", "Germany",
       "India", "Indonesia", "Italy", "Japan", "Mexico", "Korea, Rep.", "Russian Federation",
       "Saudi Arabia", "South Africa", "Turkiye", "United Kingdom", "United States", "EU"]

P20 = ["China", "India", "United States", "Indonesia", "Pakistan", "Nigeria",
       "Brazil", "Bangladesh", "Russian Federation", "Mexico", "Japan", "Philippines", "Ethiopia",
       "Egypt, Arab Rep.", "Congo, Dem. Rep.", "Vietnam", "Iran, Islamic Rep.", "Turkiye", "Germany", "Thailand"]

xl = 'fertility.xlsx'
df = pd.read_excel(xl)

##########################################################################################


df1 = pd.DataFrame(columns=[str(i) for i in range(1960,2021)])
for i in range(217):
    
    fert = df.iloc[i,4:65]
    f = [0 if i == ".." else i for i in fert]
    df1.loc[len(df1)] = f

rowN = df.iloc[0:217,2]
df1.index = rowN
df1 = df1.T
EU = df1[Eu].T.describe(include='all').loc['mean']
df1.insert(len(df1), "EU", EU)


Top20 = df1.T["2020"].nlargest(20)
Bot20 = df1.T["2020"].nsmallest(32)[12:]

def start():
    print("   ")
    print("#########################################################")
    print("EU --- G20 --- 20 most populated countries")
    print("#########################################################")
    print("Top 20 most fertile, bottom 20 least fertile or anyother country ")
    print("#########################################################")
    print("   ")

    land = input("Which one do you choose?").capitalize()

    if land == "Top20":
        print(Top20)
    elif land == "Bot20":
        print(Bot20)
    else:
        if land == "G20":
            df1[G20].plot(figsize = (25,9))
        elif land == "P20":
            df1[P20].plot(figsize = (25,9))
        elif land == "Eu":
            df1[Eu].plot(figsize = (25,9))
        else:
            for i in rowN.tolist():
                if land in i:
                    df1[i].plot(figsize = (25,9))
                    
        plt.legend()
        plt.axhline(y=2.1, color="r", linestyle="dashed")

        plt.show()


start()




