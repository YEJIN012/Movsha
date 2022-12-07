import requests
import json
import os
import environ

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

TMDB_API_KEY = env('TMDB_API_KEY')
def get_movie_datas(N):
    total_data = []

    page = 1
    cnt = 0
    while cnt < N:
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={page}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            try:
                data = {
                    'genres': movie['genre_ids'],
                    'title': movie['title'].strip(),
                    'release_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'].strip(),
                    'poster_path': 'https://image.tmdb.org/t/p/w500' + movie['poster_path'],
                }

                if (data['title'] and data['release_date'] and data['popularity'] and data['vote_count'] and data['vote_average'] and data['overview'] and data['poster_path'] and data['genres']):
                    cnt += 1
                    json = {
                        'model': 'movies.movie',
                        'fields': data
                    }
                    total_data.append(json)
                
                    if cnt >= N:
                        break
            
            except Exception as e:
                print(e)
                print(movie)
                print()

        page += 1
    
    return total_data


movie_list = get_movie_datas(500)
print(len(movie_list))

with open("./movies/fixtures/movies_500.json", "w", encoding="utf-8") as w:
    json.dump(movie_list, w, indent=4, ensure_ascii=False)