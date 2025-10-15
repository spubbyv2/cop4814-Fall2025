import requests
import main_functions
from dotenv import load_dotenv
import os

load_dotenv()

news_key = os.getenv("NEWS_KEY")

url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="

final_url = url + news_key

news = requests.get(final_url).json()

main_functions.save_to_file(news, "news.json")

