import csv
import requests
from bs4 import BeautifulSoup
import datetime

list_news = []
#row = {}
categories = ["politics", "cross-strait",
              "business", "society", "sports", "sci-tech", "culture"]

print("crawing")
for c in categories:
    for m in range(3, 6):
        for d in range(1, 32):
            for p in range(1, 10000):
                
                date = "2020"+"{:02n}".format(m)+"{:02n}".format(d)
                page = date+"{:04n}".format(p)
                url = "https://focustaiwan.tw/"+c+"/"+page
                page = requests.get(url).text
                soup = BeautifulSoup(page, "lxml")
     
                if(soup.findAll("div", {"class": "face404"})):
                    break
                else:
                    text = "".join([p.text for p in soup.find_all("p")])
                    title = soup.find("span", {"class": "h1t"}).text
                    row = {}
                    row["date"] = str(m)+"/"+str(d)+"/2020"
                    row["title"]=title
                    row["text"] = text
                    row["url"] = url
                    list_news.append(row)
    
print(len(list_news))
#save to csv
csv_columns = ['date','title', 'text', 'url']
csv_file = "news_focustaiwan.csv"
print("save to csv")
try:
    with open(csv_file, 'w', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=csv_columns, lineterminator='\n')
        writer.writeheader()
        for data in list_news:
            writer.writerow(data)
except IOError:
    print("I/O error")

print("done")