import requests
import json

#TODO: fill in the FB_GROUP_ID and your access token
FB_GROUP_ID = '1834901519863165'
# get access token from
# https://developers.facebook.com/tools/explorer"
access_token = 'EAACEdEose0cBAA3ZBapZCZCymFUyVnRKc80dyuxSHXNeqH6AC1sR4UJooz721RQw2BYVCAvFZC2KiZBUJClOGJRLsEJ2vlbmMfWHmlp45unFhXnbKYCtLYhGl98vGlmuAuoa5G04U8wWzQbD7ZAtpULrbs0DQL7OzCfLqvX2c8E35EjV2XDPYbXh3bFz9qxhZCR0LYwASin766SqEZA4fmyOsw2ZARo6ZBCUfdYBa72ZCE70QZDZD'
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

#function gets data from caching or API
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
#post messages, likes, comments, subcomments, sublikes, submessages
url_params["fields"] = "message,likes{name},from,comments{from,comments{likes,message,from},message,likes}"
url_params['filter'] = 'stream'
url_params["limit"] = 200

r = requests.post('{}/feed'.format(FB_BASEURL), data={'message': 'Hello from Python File', 'access_token': access_token})
print(r.status_code)
