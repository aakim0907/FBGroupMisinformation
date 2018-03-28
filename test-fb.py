import requests
import json
import sys
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
access_token = 'EAACEdEose0cBAC1AFc6MdhgWvhZCsMPSw3WrAZB4SmenD4If6UbuCxHEfv4ifnUjHbeH48NK11g9qHg2ZB1dRkgnYv9947v2pLmPP2bnmC8NJYnf89RXwzGuXIKMrbCzcyC951tUkYYNKZALx3ZAtQ7LAVV6xE344VtYmg6QmXyjae6ZAfq0YpNbvsGExDT5IZD'
if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

FB_BASEURL = "https://graph.facebook.com/v2.12/{}".format(FB_GROUP_ID)

#function that prints json nicely (for debugging only)
def pretty(obj):
    return json.dumps(obj, sort_keys = True, indent = 2)

# Building the Facebook parameters dictionary
url_params = {}
url_params["access_token"] = access_token
url_params["fields"] = "message,link"
url_params['filter'] = 'stream'
url_params["limit"] = 200

r = getWithCaching('{}/feed'.format(FB_BASEURL), params=url_params)

#Get posts from the Facebook group
try:
    r = getWithCaching('{}/feed'.format(FB_BASEURL), params=url_params)
    fb_posts = json.loads(r)['data']
except:
    print('Failed to get data from group. check access token expiration')
    sys.exit(0)

#Look through every post in the feed for a URL to do action on
for post in fb_posts[:2]:
    #check for link field in post, which contains the URL attached to the post
    if 'link' in post:
        #scrape the information in the url
        text = scrape_from_url(post['link'])

        #run text through paralleldots to find keywords
        keywords = paralleldots.keywords(text)

        #go to news api to find articles
        print(get_articles(keywords))

        #use paralleldots to find the most similar article to initial url

        #choose the URL that we want to post and save in variable
        #url_to_post =

        #POST request to post the url in the group
        # r = requests.post('{}/feed'.format(FB_BASEURL), data={'message': url_to_post, 'access_token': access_token})
        # print(r.status_code)
