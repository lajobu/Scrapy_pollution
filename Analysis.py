import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from time import gmtime, strftime
pd.set_option("display.precision", 2)

'''
Once the spider pollution is run, this script will filter the data and give an output for the analysis
We will receive four outputs:
    1) Summary of all the data 
    2) Summary of the data filtered by european countries
    3) A .png file with a boxplot of the pollution for the european countries
'''

df = pd.read_csv(
    'WS_project/Data/pollution.csv') #We take the output from the spider pollution as pandas data frame

#We separate the columns of the data frame in list
list_text = list(df['text']) #We will create text, city and country columns
list_pollution = list(df['pollution'])
list_date = list(df['date'])

#As list_text has several items separated by comma, we split the data
list1 = []
for i in range(len(list_text)):
    a = str(list_text[i]).split(',', 20)
    list1.append(a)

#We take the round average of all the split
r = 0
for i in range(len(list1)):
    r += len(list1[i])
mean = round(r/(len(list1)))

'''We are just taking the text values with the same length as the rounded average length, there are some columns with larger length, and all
of them supposed to have the length. This bug comes from the fact that the page is JS react with the local aphabet, for example: for Chinese
countries, the names are weitten in chinese, with chinese signs, the same thing as other many languagues, when reading by python generate
weird signs, for example commas. It was decided to not take into consideration this values (not a lot of them), as we wanted to minimize
the manual work, cleaning manually this data'''
list_prob = [] #It will take the position of the problematic values
for i in range(len(list1)):
    if len(list1[i]) == mean:
        i += 1
    else:
        list_prob.append(i)

#With the position of the problematic values, we create the list of columns firstly pollution and date
list2 = []
pollution = []
date = []
for i in range(len(list1)):
    if i not in list_prob:
        list2.append(list1[i])
        pollution.append(list_pollution[i])
        date.append(list_date[i])

#Secondly text, country and city, that comes from the item text in the spider pollution
value = ["µg/m³"] * int(len(list2))
text = []
country = []
city = []
for i in range(len(list2)):
    text.append(list2[i][0])
    country.append(list2[i][3])
    city.append(list2[i][6])

result = pd.concat([pd.DataFrame(text), pd.DataFrame(city), pd.DataFrame(
    country), pd.DataFrame(pollution), pd.DataFrame(value), pd.DataFrame(date)], axis=1) #We create a data frame withh 5 columns, result
result.columns = ['Text', 'Country', 'City', 'Pollution', 'Value', 'Date'] #To setup the name of teh columns

#Filter the data:
#Because there were negative values like -999:
result = result[result['Pollution'] > 0] #To take just the positive values from pollution
result.round() #To round the pollution values
result['Date'] = pd.to_datetime(result['Date'], format='%Y/%m/%d %H:%M') #To convert the column Date to datetime, we will be able to filter like that
#Because there were old dates, like year 2015, 2018... It looks like that the old stations there were not deleated from the website:
result = result[result['Date'] > '2020/01/01 00:00'] #To take the data only with updated information, from the year 2020

#It prints a summary of the filtered data:
print("Result all countries:")
print(result.describe())

#It saves the filtered data as csv file:
result.to_csv('result_pollution.csv', index=False)

#We wuill create a list of european countries to analize it further:
eur_countries = ["Austria", "Belgium", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia",
                 "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Norway", "Poland", "Slovakia", "Portugal", "Slovenia", "Spain", "Sweden", "Switzerland"]

#To create a new data frame with the data of the european countries:
result_europe = result[result['Country'].isin(eur_countries)]

#It prints a summary of the filtered data by european countries:
print("Result european countries:")
print(result_europe.describe())

#We will create a seaburn boxplot of the european countries pollution:
sns.set(style="ticks", palette="muted", color_codes=True)
plt.figure(figsize=(18, 12))
ax = sns.boxplot(x="Pollution", y="Country", data=result_europe,
                 color="c")
sns_plot = sns.stripplot(x="Pollution", y="Country", data=result_europe,
                         jitter=False, size=5, color=".3", linewidth=1)
sns.despine(trim=True)

#The boxplot graph will be saved as png file:
time = strftime("%Y-%m-%d %H.%M", gmtime())
fig = sns_plot.get_figure()
fig.savefig(
    "pollution_european_countries." + time + ".png")
