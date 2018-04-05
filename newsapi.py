import requests
import json
from datetime import date, timedelta
import config

a = {'keywords': [{'confidence_score':0.45759, 'keyword': 'Prime Minister Narendra Modi'}, {'confidence_score':0.95, 'keyword':'bitcoin'}, {'confidence_score':0.945534, 'keyword':'mining'}],'usage':'asdfasd'}

def get_articles(keyword_obj):
  keywords = " OR ".join([keyword['keyword'] for keyword in keyword_obj['keywords'] if keyword.get('confidence_score') > 0.97])
  week_ago = date.today()-timedelta(days=7)
  
  baseurl = ('https://newsapi.org/v2/everything?')
  query = 'q={}&'.format(keywords)
  fromdate = 'from={}&'.format(week_ago)
  moreurl = ('sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
            'sortBy=relevancy&'
            'apiKey={}'.format(config.newsapi_api_key))
  response = requests.get(baseurl+query+fromdate+moreurl).json()

  return [article['url'] for article in response['articles']]

print (get_articles(a))

# url = ('https://newsapi.org/v2/everything?'
#        'q=bitcoin&'
#        'from=2018-03-17&'
#        'sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
#        'sortBy=relevancy&'
#        'apiKey={}'.format(config.newsapi_api_key))
# response = requests.get(url).json()

# def pretty(obj):
#   return json.dumps(obj, sort_keys = True, indent = 2)

# A JSON object with three keys: articles, status, totalResults
# print (pretty(response))
