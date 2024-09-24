import requests

class theMovieDB:    
    def __init__(self):
        self.api_url="http://api.themoviedb.org/3"
        self.api_key="384b51eff1d3ce791b5acb1ef51588d7"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        if response.status_code == 200:
            return response.json()
    
    def getSearch(self,keyword):
        response=requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        if response.status_code == 200:
            return response.json()
        
movieApi = theMovieDB()  # Created an object from the class

while True:
    secim=input("1-Popular Movies\n2-Search Movies\n3-Exit\nSecim: ")
    if(secim=="3"):
        break
    else:
        if secim=="1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        elif secim=="2":
            keyword=input('keyword: ')
            movies = movieApi.getSearch(keyword)
            for movie in movies['results']:
                print(movie['name'])