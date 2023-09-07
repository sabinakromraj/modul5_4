from datetime import datetime
import random

class Movie:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views +=1

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Series(Movie):
    def __init__(self, title, release_year, genre, season, episode):
        super().__init__(title, release_year, genre)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"
    
def get_movies(media_library):
    movies = [media for media in media_library if type(media) == Movie]
    return sorted(movies, key=lambda x: x.title)

def get_series(media_library):
    series = [media for media in media_library if isinstance(media, Series)]
    return sorted(series, key=lambda x: x.title)
    
def search(query):
    results = [media for media in media_library if query in media.title]
    return results
    
def generate_views(media_library):
    media = random.choice(media_library)
    views = random.randint(1, 100)
    media.views += views

def run_generate_views(media_library, num_runs=10):
    for i in range(num_runs):
        generate_views(media_library)

def get_top_titles(media_library, count):
    sorted_media = sorted(media_library, key=lambda x: x.views, reverse=True)
    return sorted_media[:count]


if __name__ == "__main__":
    print("Biblioteka filmów")
                
media_library = [
    Movie("Pulp Fiction", 1994, "Crime"),
    Movie("The Shawshank Redemption", 1994, "Drama"),
    Movie("The Green Mile", 1999, "Drama"),
    Movie("Forrest Gump", 1994, "Drama"),
    Series("Breaking Bad", 2008, "Crime", 1, 1),
    Series("Game of Thrones", 2011, "Fantasy", 2, 2),
    Series("House M.D.", 2004, "Drama/Comedy", 3, 3),
    Series("Stranger Things", 2016, "Drama/Horror/Sci-Fi", 1, 1)
]

run_generate_views(media_library, 10)

current_date = datetime.now().strftime("%d.%m.%Y")
print(f"Najpopularniejsze filmy i seriale dnia {current_date}:")

top_titles = get_top_titles(media_library, 3)
for idx, title in enumerate(top_titles, start=1):
    print(f"{idx}. {title} ({title.views} odtworzeń)")
