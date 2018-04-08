import requests
import json
import sys
import retinasdk
import config
import webbrowser

#from our code
from scraper import scrape_from_url
from cortical import get_keywords
from newsapi import get_article_urls
from caching import getWithCaching


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
    keywords = get_keywords(text)
    #get news article urls from keywords
    urls_to_post = get_article_urls(keywords)
    return urls_to_post

#example of it fetching an article
article = 'https://www.buzzfeed.com/michaelblackmon/new-york-city-police-are-investigating-a-scuffle-involving?bfsplash&utm_term=.wqEm1qPZw#.nfxKeO6X7'
for url in get_similar_urls(article)[:5]:
    print(url)
    # opens it in browser so you can see the news articles right away and see if relevant
    # webbrowser.get().open(url)

# Building the Facebook parameters dictionary
# url_params = {}
# url_params["access_token"] = access_token
# url_params["fields"] = "message,link"
# url_params['filter'] = 'stream'
# url_params["limit"] = 200
#
# #Get posts from the Facebook group
# try:
#     r = getWithCaching('{}/feed'.format(FB_BASEURL), params=url_params)
#     fb_posts = json.loads(r)['data']
# except:
#     print('Failed to get data from group. check access token expiration')
#     sys.exit(0)

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
