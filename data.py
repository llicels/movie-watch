import requests
import vidsrc_search
def popularMovies():
    

    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjcxOWViYTE0YTJhNzhlODU1Y2ZkOWRiZWI4YWMxYiIsIm5iZiI6MTcyMDkwNTY3MS4zMjk3ODksInN1YiI6IjY2OTJlZWY5MWZlYjk4NDZmNzg5M2MxNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.EZlh_1YVpTg-K-NUJKrDr3MoqTH4Cx9YgMW3KCIPkak"
    }

    response = requests.get(url, headers=headers).json()

    numberOfResults = len(response["results"])

    movies = [None]*numberOfResults
    a = vidsrc_search()
    print(a)

    for i in range (numberOfResults):
        image = f"http://image.tmdb.org/t/p/w500/{response["results"][i]["poster_path"]}"
        id = response["results"][i]["id"]
        link = f"https://vidsrc.to/embed/movie/{id}"
        movies[i]=[response["results"][i]["title"], image, link]

    return(movies)

popularMovies()