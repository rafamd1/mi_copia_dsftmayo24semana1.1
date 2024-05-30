#!/usr/bin/env python
# coding: utf-8

# ## Web scrapping de IMDB

# Descarga la información correspondiente y guarda en un dataframe el [top de las 250 películas](https://www.imdb.com/chart/top/?ref_=nv_mv_250) mediante webscrapping. Después crea un script en python para realizar la tarea.
# 
# Obtén:
# * Título
# * Año
# * Duración
# * Posición
# * Rating

# In[182]:


# Si la petición te devuelve un 403, puedes probar con:
get_ipython().system(' pip install fake-useragent')
from fake_useragent import UserAgent
ua = UserAgent()
headers = {'User-Agent': ua.random}
response = requests.get(url, headers=headers)


# In[183]:


from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
import numpy as np

pd.set_option('max_colwidth', 800)


# In[184]:


url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url, headers=headers)


# In[185]:


print(response)


# In[186]:


html = response.content


# In[187]:


soup = bs(html, 'html.parser')


# In[188]:


print(soup)


# In[189]:


soup.title


# In[190]:


soup.h1


# In[191]:


soup.h1.get_text()


# In[192]:


soup.a


# In[193]:


soup.a['href']


# In[194]:


soup.find("a")


# In[195]:


soup.find_all('a')


# In[196]:


all_a = soup.find_all('a')
for a in all_a[:5]:
    print(a)


# In[197]:


all_a = soup.find_all('a')
for a in all_a[:5]:
    print(a.get_text())


# In[198]:


all_a = soup.find_all('a')
for a in all_a[:5]:
    print(a['href'])


# In[199]:


soup.find("a").find('div')


# In[200]:


ft= []
titulos= []


for elemento in soup.find_all("div", class_="ipc-metadata-list-summary-item__c"):
    full_text= elemento.find('a').get_text()
    title= full_text.split('. ', 1)[1]
    titulos.append(title)
    ft.append(full_text)



ft


# In[201]:


titulos


# In[202]:


posicion= []


for elemento in soup.find_all("div", class_="ipc-metadata-list-summary-item__c"):
    full_text= elemento.find('a').get_text()
    rking= full_text.split('. ',1)[0]
    print(rking)
    posicion.append(rking)


posicion



# In[203]:


posicion= np.arange(1,251)
posicion


# In[204]:


fecha= []

for elemento in soup.find_all("span", class_="sc-b189961a-8 kLaxqf cli-title-metadata-item"):
    if len(elemento.get_text()) == 4:
        fecha.append(elemento.get_text())
    else:
        continue

fecha


# In[205]:


for elemento in soup.find_all("span", class_="sc-b189961a-8 kLaxqf cli-title-metadata-item"):
    print(elemento.get_text())


# In[206]:


duracion= []

for elemento in soup.find_all("span", class_="sc-b189961a-8 kLaxqf cli-title-metadata-item"):
    if 'h' in elemento.get_text() or len(elemento.get_text()) == 5:
        duracion.append(elemento.get_text())
    else:
        continue

duracion


# In[207]:


rating= []

for elemento in soup.find_all("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"):
    rating.append(elemento.get_text()[:3])

rating


# In[208]:


peliculas = {
    'Titulo': titulos,
    'Año': fecha,
    'Duración': duracion,
    'Posicion': posicion,
    'Rating': rating
}


# In[209]:


len(posicion)


# In[210]:


len(rating)


# In[211]:


len(titulos)


# In[212]:


len(ranking)


# In[213]:


len(duracion)


# In[214]:


peliculas2= pd.DataFrame(peliculas)

peliculas2

