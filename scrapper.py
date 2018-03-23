import requests
from bs4 import BeautifulSoup
import paralleldots

# Insert URL
indiatv = "https://www.indiatvnews.com/entertainment/celebrities-okay-for-outsiders-to-be-discriminated-against-in-film-industry-kangana-ranaut-433170"
bbc = "http://www.bbc.com/news/world-us-canada-43444791"
usatoday = "https://www.usatoday.com/story/tech/talkingtech/2018/01/31/facebook-says-no-cryptocurrency-ads-citing-misleading-and-deceptive-practices/1082117001/?utm_source=google&utm_medium=amp&utm_campaign=speakabl"
economist = "https://www.economist.com/news/finance-and-economics/21735055-china-has-taken-harsh-line-south-korea-contemplates-banning-bitcoin"
URL = economist

# extracter code

r = requests.get(URL)
soup = BeautifulSoup(r.content,"html.parser")
ptags = soup.find_all('p')
extracted = []
for tag in ptags:
    for x in tag.descendants:
        if len(x)>0 and str(type(x)) == "<class 'bs4.element.NavigableString'>":
            print(x)