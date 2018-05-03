
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import urllib.request
import os,sys

def scrape(manga_id):
    site_url = "https://nhentai.net/g/"
    image_url = "https://i.nhentai.net/galleries/"
    sizemanga = len(BeautifulSoup(requests.get(site_url+manga_id).content,"html.parser").find_all("div",{"class":"thumb-container"}))
    cover = BeautifulSoup(requests.get(site_url+manga_id).content,"html.parser").find("meta",  property="og:image")["content"].split("/")
    path = "./"+manga_id
    os.mkdir( path, 0o777 )
    for page in range(1,sizemanga+1): 
        urllib.request.urlretrieve(image_url+cover[-2]+"/"+str(page)+".jpg","./"+manga_id+"/"+str(page)+".jpg")
        print(str(page)+".jpg downloaded")

