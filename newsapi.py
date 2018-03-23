import requests
import json
from datetime import date, timedelta
# https://docs.python.org/3/library/datetime.html#date-objects

def get_articles(keyword_obj):
  keyword_obj = dict((k, v) for k, v in keyword_obj.items() if v >= 4)
  keywords = ",".join(keyword_obj.keys())

  week_ago = date.today() - timedelta(days=7)

  baseurl = ('https://newsapi.org/v2/everything?')
  query = 'q={}&'.format(keywords)
  fromdate = 'from={}&'.format(week_ago)
  moreurl = ('sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
            'sortBy=relevancy&'
            'apiKey=ec0b1ca2e1894f9ca009e33dfc7ef619')
  response = requests.get(baseurl+query+fromdate+moreurl).json()

  return [article['url'] for article in response['articles']]

# ORIGINAL
# url = ('https://newsapi.org/v2/everything?' 
#        'q=bitcoin&'
#        'from=2018-01-10&'
#        'sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
#        'sortBy=relevancy&'
#        'apiKey=ec0b1ca2e1894f9ca009e33dfc7ef619')
# response = requests.get(url).json()

# def pretty(obj):
#   return json.dumps(obj, sort_keys = True, indent = 2)

# A JSON object with three keys: articles, status, totalResults
# print (pretty(response))