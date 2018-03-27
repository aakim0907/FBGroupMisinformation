import requests
import json
from datetime import date, timedelta
# https://docs.python.org/3/library/datetime.html#date-objects

a = {'keywords': [{'confidence_score':0.45759, 'keyword': 'Prime Minister Narendra Modi'}, {'confidence_score':0.95, 'keyword':'bitcoin'}, {'confidence_score':0.945534, 'keyword':'mining'}],'usage':'asdfasd'}

def get_articles(keyword_obj):
  keywords = " OR ".join([keyword['keyword'] for keyword in keyword_obj['keywords'] if keyword.get('confidence_score') > 0.9])
  week_ago = date.today()-timedelta(days=7)
  print (keywords)
  baseurl = ('https://newsapi.org/v2/everything?')
  query = 'q={}&'.format(keywords)
  fromdate = 'from={}&'.format(week_ago)
  moreurl = ('sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
            'sortBy=relevancy&'
            'apiKey=ec0b1ca2e1894f9ca009e33dfc7ef619')
  response = requests.get(baseurl+query+fromdate+moreurl).json()

  return [article['url'] for article in response['articles']]

# print (get_articles(a))

# url = ('https://newsapi.org/v2/everything?'
#        'q=bitcoin&'
#        'from=2018-03-17&'
#        'sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
#        'sortBy=relevancy&'
#        'apiKey=ec0b1ca2e1894f9ca009e33dfc7ef619')
# response = requests.get(url).json()

# def pretty(obj):
#   return json.dumps(obj, sort_keys = True, indent = 2)

# A JSON object with three keys: articles, status, totalResults
# print (pretty(response))
