import requests
from bs4 import BeautifulSoup
import pandas as pd
link = requests.get('https://ana.press/')
soup_link = BeautifulSoup(link.text, 'html.parser')
news = pd.DataFrame()
title_original = soup_link.find('div', {'class': "section-3"})

for i in range(0, 15):
    try:
        address = title_original.findAll('a', {'class': "d-block"})[i]
        #print(address.text)
        #print('*******************')
        news.loc[i, "address"] = address.text
        rutitr = title_original.findAll('div', {'class': "section-3-news-rutitr"})[i]
        news.loc[i, "rutitr"] = rutitr.text
        titr = title_original.findAll('h2', {'class': "section-3-news-titr"})[i]
        print(titr.text)
        news.loc[i, "titr"] = titr.text
        print(i)
        subtitle = title_original.findAll('div', {'class': "section-3-news-subtitle"})[i]
        news.loc[i, "subtitle"]  = subtitle.text
    except:
        pass



