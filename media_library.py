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
    
class MediaLibrary:
    def __init__(self):
        self.media_collection = []
    
    def add_media(self, media):
        self.media_collection.append(media)

    def play_media(self, title):
        for media in self.media_collection:
            if media.title == title:
                media.play()

    def get_movies(library):
        movies = [media for media in library.media_collection if isinstance(media, Movie)]
        movies.sort(key=lambda x: x.title)
        return movies

    def get_series(library):
        series = [media for media in library.media_collection if isinstance(media, Series)]
        series.sort(key=lambda x: x.title)
        return series  
    
    def search(library, query):
        results = [media for media in library.media_collection if query in media.title]
        return results
    
    def generate_views(library):
        for i in range(10):
            media = random.choice(library.media_collection)
            views = random.randint(1, 100)
            media.views += views

    def get_top_titles(self, count):
        sorted_media = sorted(self.media_collection, key=lambda x: x.views, reverse=True)
        return sorted_media[:count]


if __name__ == "__main__":
    print("Biblioteka filmów")
                
    library = MediaLibrary()

    movie1 = Movie("Pulp Fiction", 1994, "Crime")
    movie2 = Movie("The Shawshank Redemption", 1994, "Drama")
    movie3 = Movie("The Green Mile", 1999, "Drama")
    movie4 = Movie("Forrest Gump", 1994, "Drama")
    series1 = Series("Breaking Bad", 2008, "Crime", 1, 1)
    series2 = Series("Game of Thrones", 2011, "Fantasy", 2, 2)
    series3 = Series("House M.D.", 2004, "Drama/Comedy", 3, 3)
    series4 = Series("Stranger Things", 2016, "Drama/Horror/Sci-Fi", 1, 1)

    library.add_media(movie1)
    library.add_media(movie2)
    library.add_media(movie3)
    library.add_media(movie4)
    library.add_media(series1)
    library.add_media(series2)
    library.add_media(series3)
    library.add_media(series4)

    library.generate_views()

    current_date = datetime.now().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {current_date}:")

    top_titles = library.get_top_titles(3)
    for idx, title in enumerate(top_titles, start=1):
        print(f"{idx}. {title} ({title.views} odtworzeń)")