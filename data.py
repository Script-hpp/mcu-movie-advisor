import json
class Marvel:
    def __init__(self, title,poster,date,overview,vote_average):
        self.title = title
        self.poster = poster
        self.date = date
        self.overview = overview
        self.vote_average = vote_average
    
    movie_titles = []
    movie_backgrounds = []
    movie_overview = []
    movie_vote = []
    movie_release_date = []


    def get_movie_backgrounds(self):
        with open('movies_data.json', 'r') as f:
                data = json.load(f)
                for movie in data:
                    self.movie_backgrounds.append(movie["poster_path"])

    def get_titles(self):
        with open('movies_data.json', 'r') as f:
                data = json.load(f)
                for movie in data:
                    self.movie_titles.append(movie["original_title"])

    def get_overview(self):
        with open('movies_data.json', 'r') as f:
                data = json.load(f)
                for movie in data:
                    self.movie_overview.append(movie["overview"])

    def get_userscore(self):
        with open('movies_data.json', 'r') as f:
                data = json.load(f)
                for movie in data:
                    self.movie_vote.append(movie["vote_average"])

    def get_release_date(self):
        with open('movies_data.json', 'r') as f:
                data = json.load(f)
                for movie in data:
                    self.movie_release_date.append(movie["release_date"])

    
