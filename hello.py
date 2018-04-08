import requests
import json
import sys
import retinasdk
import config
import webbrowser
from bs4 import BeautifulSoup

#from our code
from scraper import scrape_from_url
from cortical import get_keywords
from newsapi import get_article_urls
from caching import getWithCaching


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(results=None):
    if request.args.get('link', None):
        article = request.args.get('link', None)
        results = get_similar_urls(article)[:5]
        # for result in results:
        #     r = requests.get(result)
        #     soup = BeautifulSoup(r.content,"html.parser")
        #     title = soup.title.string
    return render_template('index.html', results=results)


#function that, given a url, finds similar urls
def get_similar_urls(url):
    #scrape text from url
    text = scrape_from_url(url)
    #get keywords from text
    keywords = get_keywords(text)
    #get news article urls from keywords
    urls_to_post = get_article_urls(keywords)
    return urls_to_post

#example of it fetching an article
# article = request.args.get('link', None)
# 'https://www.buzzfeed.com/michaelblackmon/new-york-city-police-are-investigating-a-scuffle-involving?bfsplash&utm_term=.wqEm1qPZw#.nfxKeO6X7'
# for url in get_similar_urls(article)[:5]:
#     print(url)
#     opens it in browser so you can see the news articles right away and see if relevant
#     webbrowser.get().open(url)

if __name__ == "__hello__":
    app.run()