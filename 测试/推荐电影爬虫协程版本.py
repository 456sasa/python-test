import asyncio
import aiohttp
from aiohttp import connector
from bs4 import BeautifulSoup


header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

async def fetch_content(url):
    async with aiohttp.ClientSession{
        headers=header，connector=aiohttp.connector.TCPConnector(ssl=False)
    }as session:
         async with session.get(url) as response: 
             return await response.text()

async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page,'lxml')

    movie_names, urls_to_fetch, movie_dates = [], [], []
    all_movies = init_soup.find('div',id="showing-soon")        

    for each_movie in all_movies.find_all('div',class_="item"):
        