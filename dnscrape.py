
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import urllib.request
import os,sys
import json
# import neopdfmerge

def nhentai(manga_id):
    site_url = "https://nhentai.net/g/"
    image_url = "https://i.nhentai.net/galleries/"
    sizemanga = len(BeautifulSoup(requests.get(site_url+manga_id).content,"html.parser").find_all("div",{"class":"thumb-container"}))
    cover = BeautifulSoup(requests.get(site_url+manga_id).content,"html.parser").find("meta",  property="og:image")["content"].split("/")
    path = "./nhentai/"+manga_id
    os.mkdir( path, 0o777 )
    for page in range(1,sizemanga+1): 
        urllib.request.urlretrieve(image_url+cover[-2]+"/"+str(page)+".jpg","./nhentai/"+manga_id+"/"+str(page)+".jpg")
        print(str(page)+".jpg downloaded")
#     neopdfmerge.neoconvert("nhentai",manga_id,sizemanga)

def erolord(manga_id):
    site_url = "http://erolord.com/doujin/"
    image_url = "http://erolord.com/images/"
    sizemanga = BeautifulSoup(requests.get(site_url+manga_id).content,"html.parser").find("a",{'id': 'ahr1'})["href"].split("=")[-1]
    cover = BeautifulSoup(requests.get(site_url+manga_id).content,"html.parser").find("img", {'id': 'p1'})["src"].split("/")
    path = "./erolord/"+manga_id
    os.mkdir( path, 0o777 )
    for page in range(1,int(sizemanga)+1): 
        urllib.request.urlretrieve(image_url+cover[2]+"/"+manga_id+"/"+str(page)+".jpg","./erolord/"+manga_id+"/"+str(page)+".jpg")
        print(str(page)+".jpg downloaded")
#     neopdfmerge.neoconvert("erolord",manga_id,sizemanga)

