from bs4 import BeautifulSoup
import requests
import csv
from PIL import Image, ImageDraw
from datetime import date
from instabot import Bot
import time

#IG-pw: nrleirrw
bot = Bot()
today = date.today()

zeit = requests.get("https://www.zeit.de/index").text
zeit_soup = BeautifulSoup(zeit, "lxml")

zeit_content = ""
for article in zeit_soup.find_all("article"):

    headline = article.h3
    zeit_content += str(headline)
    teaser = article.p
    zeit_content += str(teaser)

#print(zeit_content)

substring = "Corona" 
zeit_count = zeit_content.count(substring)
print(zeit_count)

#with open("record.csv", "w", newline="") as record:
#    writer = csv.writer(record)
#    writer.writerow([zeit_count, "color"])


def get_color(x): #1 is red, 100 is green
    color_list = []
    with open("colors.csv", 'r') as colors:
        reader = csv.reader(colors)
        for row in reader:
            color_list.append(row[1])

    return color_list[x-1]

#normalize count
zeit_count_normal = int(zeit_count/50*100)
print(zeit_count_normal)

img = Image.new('RGB', (500, 500), color=get_color(zeit_count_normal))
img.save(str(today)+".jpg")


bot.login(username="the_fadeout", password="nrleirrw")
time.sleep(1)
bot.upload_photo(str(today)+".jpg", caption="\"Corona\" wurde heute, "+ str(today) + ", " + str(zeit_count) +" Mal auf Zeit.de erwähnt.")
