import requests
import json
from datetime import date, timedelta
# https://docs.python.org/3/library/datetime.html#date-objects

# HANDLE INPUT 
# keyword = input("Enter keyword:")
# print (keyword)


# ORIGINAL
url = ('https://newsapi.org/v2/everything?' 
       'q=bitcoin&'
       'from=2018-01-10&'
       'sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
       'sortBy=relevancy&'
       'apiKey=ec0b1ca2e1894f9ca009e33dfc7ef619')

response = requests.get(url).json()

# W/ USER INPUT
# baseurl = ('https://newsapi.org/v2/everything?')
# query = 'q={}&'.format(keyword)
# date = 'from=2018-01-10&'
# print (date.today())
# moreurl = ('sources=the-wall-street-journal,bbc-news,the-economist,google-news,usa-today&'
#           'sortBy=relevancy&'
#           'apiKey=ec0b1ca2e1894f9ca009e33dfc7ef619')

# response = requests.get(baseurl+query+date+moreurl).json()

def pretty(obj):
  return json.dumps(obj, sort_keys = True, indent = 2)

# A JSON object with three keys: articles, status, totalResults
print (pretty(response))
