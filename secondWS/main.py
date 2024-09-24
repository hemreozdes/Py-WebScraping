import requests
from bs4 import BeautifulSoup

urlSeries = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
urlMovies= "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

headersSeries={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0"
}
headersMovies={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0"
}

htmlSeries = requests.get(urlSeries, headers=headersSeries).content
soupSeries = BeautifulSoup(htmlSeries,"html.parser")
htmlMovies=requests.get(urlMovies,headers=headersMovies).content
soupMovies=BeautifulSoup(htmlMovies,"html.parser")
options=input("What do you want to watch: Movies(M)/Series(S) ?\n")
value=int(input("How many do you want to see?\n"))

listTv=soupSeries.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=value)
listMovies=soupMovies.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=value)
if options=="S":
    for item in listTv:
        SeriesName=item.find("h3",{"class":"ipc-title__text"}).text
        SeriesPoint=item.find("span",{"class":"ipc-rating-star--rating"}).text
        SeriesPoint=float(SeriesPoint)
        print(f"{SeriesName} -> {SeriesPoint}")
elif options=="M":
    for item in listMovies:
        SeriesName=item.find("h3",{"class":"ipc-title__text"}).text
        SeriesPoint=item.find("span",{"class":"ipc-rating-star--rating"}).text
        SeriesPoint=float(SeriesPoint)
        print(f"{SeriesName} -> {SeriesPoint}")
    