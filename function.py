import requests

def get_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=93377cf8b5800e899a44d1df617bd523&language=en-US"
    response = requests.get(url).json()
    return f"http://image.tmdb.org/t/p/w500/{response['poster_path']}"

def recommend(movie, movies, similarity):
    idx = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[idx]), reverse=True, key=lambda x: x[1])
    rec_movies = []
    rec_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        rec_movies.append(movies.iloc[i[0]].title)
        rec_posters.append(get_poster(movie_id))
    return rec_movies, rec_posters
