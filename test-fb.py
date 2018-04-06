from __future__ import unicode_literals
from builtins import str
import requests
import json
import sys

#from our code
from scrapper import scrape_from_url
import paralleldots
from newsapi import get_articles
from caching import getWithCaching

#Set up paralleldots api
api_key   = "4FJEnSvGxUI6FCYl64yWK2iDE4AqZpQso150wqrilr0"
paralleldots.set_api_key(api_key)

#Group ID for a sample group
FB_GROUP_ID = '1834901519863165'
# get access token from
# https://developers.facebook.com/tools/explorer"
#TODO fill in access token
#Access token needs permission: publish actions (set to public)
access_token = 'EAACEdEose0cBAFZAr29deooLico6v4ZBccBzbmD0hw1iY63Xqb9ZAMc8zkG2cJwVacG8QlstPcqNL4ydEBUsosOmR7lYVOt9EJq5ZC2LZCHtjcPMXtMAryZAmmP2bMK8PtdPZCI8TEUixZAotWdEWoJknB1xudNGAKPzE5sXEbEvxqc2ZBIrnKYdPXY181ce8IhEZD'
if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

FB_BASEURL = "https://graph.facebook.com/v2.12/{}".format(FB_GROUP_ID)

#function that prints json nicely (for debugging only)
def pretty(obj):
    return json.dumps(obj, sort_keys = True, indent = 2)

#function that, given a url, finds similar urls
def get_similar_urls(url):
    #scrape text from url
    text = scrape_from_url(url)
    #get keywords from text
    keywords = paralleldots.keywords(text)
    #get news article urls from keywords
    urls_to_post = get_articles(keywords)
    return urls_to_post

#example
#print(get_similar_urls('http://www.bbc.co.uk/news/business-42713314'))

# Building the Facebook parameters dictionary
url_params = {}
url_params["access_token"] = access_token
url_params["fields"] = "message,link"
url_params['filter'] = 'stream'
url_params["limit"] = 200

#Get posts from the Facebook group
try:
    r = getWithCaching('{}/feed'.format(FB_BASEURL), params=url_params)
    fb_posts = json.loads(r)['data']
except:
    print('Failed to get data from group. check access token expiration')
    sys.exit(0)

#Look through every post in the feed for a URL to do action on
# for post in fb_posts:
    #check for link field in post, which contains the URL attached to the post
    # if 'link' in post:
        #scrape the information in the url
        # urls = get_similar_urls(post['link'])
        # if len(urls) > 0:
            # url_to_post = urls[0]
            #POST request to post the url in the group
            # r = requests.post('{}/feed'.format(FB_BASEURL), data={'message': url_to_post, 'access_token': access_token})
            # print(r.status_code)
