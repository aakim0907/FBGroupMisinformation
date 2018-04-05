import retinasdk
import json
import config

def get_keywords(text):
  fullClient = retinasdk.FullClient(config.cortical_api_key, apiServer="http://api.cortical.io/rest", retinaName="en_associative")
  keywords = fullClient.getKeywordsForText(text)
  return (keywords)

print (get_keywords("Iraq War Vet Who Lost His Leg in Battle Shuts Down David Hogg With Brutal Message"))