import requests
from bs4 import BeautifulSoup
from requests.models import Response

def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    init_page = requests.get(url,headers=header).content
    init_soup = BeautifulSoup(init_page,'lxml')
    movie_names, urls_to_fetch, movie_dates = [], [], []
    all_movies = init_soup.find('div',id='showing-soon')
    for each_movie in all_movies.find_all('div',class_='item'):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')
        
        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        movie_names.append(movie_name)
        urls_to_fetch.append(url_to_fetch)
        movie_dates.append(movie_date)

        response_item = requests.get(url_to_fetch,headers=header).content  
        soup_item = BeautifulSoup(response_item,'lxml')
        img_tag = soup_item.find('img')
        print(f'{movie_name} {movie_date} {img_tag}')
        
main()