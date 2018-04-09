import requests
import json
import sys
import retinasdk
import config
import webbrowser
from bs4 import BeautifulSoup

#from our code
from scraper import scrape_from_url, scrape_title
from cortical import get_keywords
from newsapi import get_article_urls, get_articles
from caching import getWithCaching


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(results=None):
    title =''
    article=''
    if request.args.get('link', None):
        article = request.args.get('link', None)
        title = scrape_title(article)

        results = get_similar_articles(article)[:5]
    return render_template('index.html', results=results, title=title, article=article)


#function that, given a url, finds similar urls
def get_similar_articles(url):
    #scrape text from url
    text = scrape_from_url(url)
    #get keywords from text
    keywords = get_keywords(text)
    #get news article urls from keywords
    articles_to_post = get_articles(keywords)
    return articles_to_post
    