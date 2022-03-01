from datetime import date

from  bs4 import BeautifulSoup
import requests

'''
year = input("which year do you want to travel to? Type the date in this format YYY-MM-DD")

response = requests.get("https://www.billboard.com/charts/hot-100" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart_element_information_song")
'''
date_entry = input("which year do you want to go to ?")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date_entry}")

soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all("h3",class_="c-title", id="title-of-a-story")
artists =soup.find_all("span",class_="c-label")

titles_name= [title.getText() for title in titles]
artist_name= [artist.getText() for artist in artists]
print(titles_name,artist_name)
