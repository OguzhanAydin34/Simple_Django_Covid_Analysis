
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def countryData(countryName=''):
       if(countryName==''):
              return 0
       path = "/Users/oguzhan/Desktop/first_project/first_app/csv/countries-aggregated.csv"
       country = pd.read_csv(path)
       titleName = str(countryName) + " Covid-19 Data"
       a=country[country.Country==countryName].plot(figsize=(10,5), x='Date', title=titleName).get_figure()
       fileName="first_app/static/first_app/images/"+str(countryName)+"Total.png"
       a.savefig(fileName)
       #plt.show()
       plt.close(a)

def countryTable(countryName=''):
       if(countryName==''):
              return 0
       path = "/Users/oguzhan/Desktop/first_project/first_app/csv/countries-aggregated.csv"
       country = pd.read_csv(path)
       country = country[country.Country == countryName][{'Date','Confirmed','Recovered','Deaths'}]
       country=country.sort_values(by='Date',ascending=False)
       return str(country.to_html(index=False,table_id = "countryData"))

def pieChart(givenDate=""):
       if(givenDate==""):
              return 0
       colors = ['#008080', '#FAEBD7', '#ADD8E6', '#E9967A', '#8B008B', '#708090', '#FFF0F5', '#000080', '#DAA520',
                 '#FFFFE0', '#4B0082', '#556B2F', '#87CEEB', '#FFFACD', '#FFFAF0', '#00008B', '#E6E6FA', '#FAEBD7',
                 '#FFC0CB', '#00CED1', '#FF69B4']
       path = "/Users/oguzhan/Desktop/first_project/first_app/csv/countries-aggregated.csv"
       country = pd.read_csv(path)
       # print(country.info())
       country = country[country.Date == givenDate]
       country = country.sort_values(by='Confirmed', ascending=False)
       arrayCountry = country.to_numpy()
       plt.figure(figsize=(20, 20))

       fig,ax1 = plt.subplots(figsize=(20, 20))
       labels = arrayCountry[-188:-168, 1]
       # -188
       values = arrayCountry[-188:-168, 2]

       other_label = "Others"
       other_value = sum(arrayCountry[-168:, 2])
       labels = np.append(labels, other_label)
       values = np.append(values, other_value)
       exp = ((0.1,) * 21)
       plt.pie(values, autopct='%.2f', colors=colors, startangle=90, explode=exp)
       plt.tight_layout()
       plt.subplots_adjust(top=0.5)
       plt.title(("Confirmed Cases Top 20 Country(" + givenDate + ")"))
       ax1.legend(labels, loc="upper right", bbox_to_anchor=(0.05, 1.), title="Countries")
       fileName = ("first_app/static/first_app/images/pie(" + str(givenDate) + ").png")
       #fileName="/Users/oguzhan/Desktop/first_project/first_app/static/first_app/images/pie(2020-05-24).png"
       plt.savefig(fileName, bbox_inches='tight')
       plt.close()

def countryDailyData(countryName=''):
       path = "/Users/oguzhan/Desktop/first_project/first_app/csv/countries-aggregated.csv"
       country = pd.read_csv(path)
       country = country[country.Country == countryName][{'Confirmed', 'Recovered', 'Deaths', 'Date'}]
       a = country[{'Confirmed', 'Recovered', 'Deaths'}]
       difference = a.diff(axis=0);
       country['Deaths'] = difference['Deaths']
       country['Recovered'] = difference['Recovered']
       country['Confirmed'] = difference['Confirmed']
       country = country.fillna(0)
       titleName = str(countryName) + " Covid-19 Daily Change Data"
       a = country.plot(figsize=(10, 5), x='Date', title=titleName).get_figure()
       fileName = "first_app/static/first_app/images/"+str(countryName)+"Daily.png"
       a.savefig(fileName)
       print(a)
       # plt.show()
       plt.close(a)

def countryInformation(countryName=''):
       path="/Users/oguzhan/Desktop/first_project/first_app/csv/covid19countryinfo.csv"
       allCountries = pd.read_csv(path)
       countryInfoAll=allCountries[(allCountries.country==countryName) & (allCountries.region.isnull())]
       countryWantedInfo=covidWant = countryInfoAll[ ['country', 'pop', 'density', 'medianage', 'urbanpop', 'quarantine', 'schools',
       'publicplace', 'gatheringlimit', 'gathering', 'sex0', 'sex14', 'sex25', 'sex54', 'sex64',
       'sex65plus', 'sexratio', 'gdp2019','healthexp']].copy()
       info_dic = dict(zip(countryWantedInfo.keys().values, countryWantedInfo.values[0]))
       return info_dic

def countriesAsOption():
       path="/Users/oguzhan/Desktop/first_project/first_app/csv/countries-aggregated.csv"
       country = pd.read_csv(path)
       country = country['Country'].unique()
       return country

def dateAsOption():
       path = "/Users/oguzhan/Desktop/first_project/first_app/csv/countries-aggregated.csv"
       country = pd.read_csv(path)
       date = country['Date'].unique()
       return date

'''def importBasemap(givenDate=''):
       givenDate='2020-05-10'
       fig = plt.figure(figsize=(24, 12))
       # taking country datasets
       path = "/Users/oguzhan/Desktop/first_project/first_app/csv/countries-aggregated.csv"
       covid = pd.read_csv(path)
       covid = covid[covid.Date == givenDate]
       covid.index = covid.Country
       covid = covid.drop(columns=['Date', 'Country'], axis=1)
       lat_lon = pd.read_csv('lat_long.csv', engine='python')
       lat_lon.set_index("name", inplace=True)
       covid = covid.join(lat_lon, how='inner')
       print(covid)
       # map specifications
       map = Basemap(projection='robin', lon_0=0, resolution='c')
       map.fillcontinents(zorder=0)
       map.drawcoastlines()
       map.drawcountries(linewidth=1)
       map.drawmapboundary(fill_color='#2e85f0')
       map.fillcontinents(color='#a4b3a6', lake_color='#2e85f0')
       map.drawcoastlines()
       # putting data to arrays
       lons = np.array(covid.longitude)
       lats = np.array(covid.latitude)
       cases = np.array(covid.Confirmed.apply(lambda x: x / 40))
       deaths = np.array(covid.Deaths.apply(lambda x: x / 40))
       places = np.array(covid.index)
       # mapping coordinates
       x, y = map(lons, lats)
       # drawing circles for confirmed cases and deaths
       map.scatter(x, y, s=cases, c='y', alpha=0.4, zorder=3)
       map.scatter(x, y, s=deaths, c='r', alpha=0.6, zorder=3)
       # plot the graph
       plt.title("World Coronavirus Cases(Yellow) and Deaths(Red)", fontsize=22)
       plt.show()
       plt.close()'''
