import requests
import json
import sys
from scrapper import scrape_from_url
import paralleldots
from newsapi import get_articles

#Set up paralleldots api
api_key   = "4FJEnSvGxUI6FCYl64yWK2iDE4AqZpQso150wqrilr0"
paralleldots.set_api_key(api_key)



#Group ID for a sample group
FB_GROUP_ID = '1834901519863165'
# get access token from
# https://developers.facebook.com/tools/explorer"
#TODO fill in access token
#Access token needs permission: publish actions (set to public)
access_token = 'EAACEdEose0cBAE33UL0Yo3lQzZCbORxojsMqSAMZA1XJLIqmd6eSYhZCIHXpQxVsKMFdPy2Fb8JoRiAUT9bFP0cqXz3Vadt2qIWHF4LFVXrgegiZCypigcCTDNmRftEm8FVOrTn37MmHiohxIs7GPMwEEHs06YK39fwwrR6qx26tEIHRaXQHZA5jjy1u6O5sZD'
if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

FB_BASEURL = "https://graph.facebook.com/v2.12/{}".format(FB_GROUP_ID)
CACHE_FNAME = 'cache.json'

#function that prints json nicely (for debugging only)
def pretty(obj):
    return json.dumps(obj, sort_keys = True, indent = 2)

#open cache file
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICTION = json.loads(cache_contents)
except:
    CACHE_DICTION = {}

#function gets data from caching or API for get requests
def getWithCaching(baseURL, params = {}):
    req = requests.Request(method = 'GET', url = baseURL, params = sorted(params.items()))
    prepped = req.prepare()
    fullURL = prepped.url

    # if we haven't seen this URL before
    if fullURL not in CACHE_DICTION:
        # make the request and store the response
        response = requests.Session().send(prepped)
        CACHE_DICTION[fullURL] = response.text

        # write the updated cache file
        cache_file = open(CACHE_FNAME, 'w')
        cache_file.write(json.dumps(CACHE_DICTION))
        cache_file.close()

    # if fullURL WAS in the cache, CACHE_DICTION[fullURL] already had a value
    # if fullURL was NOT in the cache, we just set it in the if block above, so it's there now
    return CACHE_DICTION[fullURL]

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
