from data import Marvel
from flask import Flask, render_template
from random import randint
import sys

marvel = Marvel("original_title", "poster_path", "release_date", "overview", "vote_average")

marvel.get_movie_backgrounds();
marvel.get_titles();
marvel.get_overview();
marvel.get_userscore();
marvel.get_release_date();
app = Flask(__name__)
 

@app.route('/')
def index():
    random_index = randint(0, len(marvel.movie_backgrounds) - 1)
    movie_background_url = marvel.movie_backgrounds[random_index]
    title = marvel.movie_titles[random_index]
    overview = marvel.movie_overview[random_index]
    user_score = marvel.movie_vote[random_index]
    date = marvel.movie_release_date[random_index]

    print(title, file=sys.stderr)
    return render_template('index.html', background_image_url=movie_background_url, title=title , overview=overview, user_score=user_score, date=date)
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()