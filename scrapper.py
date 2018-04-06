import requests
from bs4 import BeautifulSoup

# Insert URL
indiatv = "https://www.indiatvnews.com/entertainment/celebrities-okay-for-outsiders-to-be-discriminated-against-in-film-industry-kangana-ranaut-433170"
bbc = "http://www.bbc.com/news/world-us-canada-43444791"
usatoday = "https://www.usatoday.com/story/tech/talkingtech/2018/01/31/facebook-says-no-cryptocurrency-ads-citing-misleading-and-deceptive-practices/1082117001/?utm_source=google&utm_medium=amp&utm_campaign=speakabl"
economist = "https://www.economist.com/news/finance-and-economics/21735055-china-has-taken-harsh-line-south-korea-contemplates-banning-bitcoin"


# extracter code
def scrape_from_url(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    title = soup.title.string
    print('title is ', title)
    #get all text in h1s
    h1tags = soup.find_all('h1')
    extracted = []
    for h1 in h1tags:
        for x in h1.descendants:
                if len(x) > 0 and str(type(x)) == "<class 'bs4.element.NavigableString'>":
                    extracted.append(x)
    h1_string = " ".join(extracted)
    print('h1s are ', h1_string)
    #cross check title with h1 and only include those that are in both
    title_words = title.split()
    h1_words = h1_string.split()
    headline = " ".join([word for word in title_words if word in h1_words])
    return headline

# print(scrape_from_url(economist))
