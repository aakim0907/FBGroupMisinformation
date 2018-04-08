import requests
import json
from datetime import date, timedelta
import config

a = {'keywords': [{'confidence_score':0.45759, 'keyword': 'Prime Minister Narendra Modi'}, {'confidence_score':0.95, 'keyword':'bitcoin'}, {'confidence_score':0.945534, 'keyword':'mining'}],'usage':'asdfasd'}
b = ['vet', 'iraq', 'leg', 'david', 'message', 'hogg']

def get_article_urls(keywords):
  week_ago = date.today()-timedelta(days=7)

  baseurl = ('https://newsapi.org/v2/everything?')
  query = 'q={}&'.format(" OR ".join(keywords))
  fromdate = 'from={}&'.format(week_ago)
  moreurl = ('sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
            'sortBy=relevancy&'
            'apiKey={}'.format(config.newsapi_api_key))
  response = requests.get(baseurl+query+fromdate+moreurl).json()

  return [article['url'] for article in response['articles']]

# print (get_article_urls(b))

def get_articles(keywords):
  week_ago = date.today()-timedelta(days=7)

  baseurl = ('https://newsapi.org/v2/everything?')
  query = 'q={}&'.format(" OR ".join(keywords))
  fromdate = 'from={}&'.format(week_ago)
  moreurl = ('sources=the-wall-street-journal,bbc-news,the-economist,usa-today&'
            'sortBy=relevancy&'
            'apiKey={}'.format(config.newsapi_api_key))
  response = requests.get(baseurl+query+fromdate+moreurl).json()

  return [{'url': article['url'], 'title': article['title']} for article in response['articles']]

# print (get_articles(b))

# url = ('https://newsapi.org/v2/everything?'
#        'q=bitcoin&'
#        'from=2018-04-01&'
#        'sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
#        'sortBy=relevancy&'
#        'apiKey={}'.format(config.newsapi_api_key))
# response = requests.get(url).json()

# def pretty(obj):
#   return json.dumps(obj, sort_keys = True, indent = 2)

# A JSON object with three keys: articles, status, totalResults
# print (pretty(response))
