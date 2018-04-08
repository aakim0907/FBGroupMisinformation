# FBGroupMisinformation
Given a url to a news article, this program gives you links to five similar articles, but from more neutral, reputable sources.

This program requires the following to be pip installed:
* requests
* flask
* retinasdk
* bs4

You need API keys from:
* newsapi
* cortical

Put these API keys into a file called `config.py` and insert these two lines in the file, replacing your api keys with the strings:
```
newsapi_api_key = "your api key here"
cortical_api_key = "your api key here" 
```

To run this program, use the command `python3 -m flask run` on terminal (`py -m flask run` on Windows), and follow the instructions.
