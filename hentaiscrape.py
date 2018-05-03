import requests
from bs4 import BeautifulSoup
import urllib.request
import os

# declaration section
main_url = "http://erolord.com/view.php?g=1&d=1160533&m=40"
manga_title = "Wingding Orgy: Hot Tails Extreme #5 [English]"
first_page = 1
number_of_page = 41

page = requests.get(main_url)
soup = BeautifulSoup(page.content, 'html.parser')
img = soup.find(id="slide_show")['src']
name = img.split("/")
path = img.strip(name[-1])
print(path)


if not os.path.exists(manga_title):
	os.makedirs(manga_title)
for x in range(1,number_of_page):
	url = "http://erolord.com/"+path+str(x)+".jpg"
	# print(url)
	urllib.request.urlretrieve(url, manga_title+"/"+name[-2]+"_"+str(x)+".jpg")

print("Done Scrap : "+manga_title)
