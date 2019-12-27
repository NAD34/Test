from .config import movies_api
import requests
from bs4 import BeautifulSoup

def movies_url():
	url = BeautifulSoup(requests.get(movies_api).text, 'lxml')
	return url

def html_movies():
	films = movies_url().find('div', class_='events-block js-cut_wrapper').find_all('li')
	movies_list = list()

	for i in films:
	    box = dict()
	    box['name'] = i.find('img').get('alt')
	    box['link'] = i.find('a').get('href')
	    box['image'] = i.find('img').get('src')
	    box['info'] = i.find('div').find('p').text
	    movies_list.append(box)
	return movies_list

def bot_movies():
	url = movies_url()
	articles = url.find_all('ul', {'class': ['b-lists list_afisha col-5']})
	return [art.find('a', {'class': ['name']}).find('span').get_text() for art in articles]
