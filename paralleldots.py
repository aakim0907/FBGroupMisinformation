import requests
import json
import paralleldots

PARALLELDOTS_KEY = '4FJEnSvGxUI6FCYl64yWK2iDE4AqZpQso150wqrilr0'

paralleldots.set_api_key(PARALLELDOTS_KEY)

def get_similarity( text_1, text_2 ):
	api_key = get_api_key()
	if not api_key == None:
		if type( text_1 ) != str or type( text_2 ) != str:
			return { "Error": "Input must be a string." }
		elif text_1 == "" or text_2 == "":
			return { "Error": "Input string cannot be empty." }
		url = "http://apis.paralleldots.com/v3/similarity"
		r =  requests.post( url, params= { "api_key": api_key, "text_1": text_1, "text_2": text_2 } )
		if r.status_code != 200:
			return { "Error": "Oops something went wrong!" }
		r = json.loads( r.text )
		return r
	else:
return { "Error": "API key does not exist" }