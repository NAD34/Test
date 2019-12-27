import datetime
from flask import render_template, url_for, Flask
from component import html_movies, url_money, get_weather_city

tok = Flask(__name__)

@tok.route('/')
@tok.route('/window')
def window():
    return render_template('window.html')

@tok.route('/courses')
def courses():
    return render_template('courses.html', data_now = datetime.datetime.now().date(), url_money = url_money())

@tok.route('/movies')
def movies():
    return render_template('movies.html', data_now = datetime.datetime.now().date(), html_movies = html_movies())

@tok.route('/weather')
def weather():
    return render_template('weather.html', data_now = datetime.datetime.now().date(), data_weather = get_weather_city())
print(get_weather_city())


if __name__ == "__main__":
    tok.run(debug=True)