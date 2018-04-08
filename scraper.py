import requests
from bs4 import BeautifulSoup

# Insert URL
indiatv = "https://www.indiatvnews.com/entertainment/celebrities-okay-for-outsiders-to-be-discriminated-against-in-film-industry-kangana-ranaut-433170"
bbc = "http://www.bbc.com/news/world-us-canada-43444791"
usatoday = "https://www.usatoday.com/story/tech/talkingtech/2018/01/31/facebook-says-no-cryptocurrency-ads-citing-misleading-and-deceptive-practices/1082117001/?utm_source=google&utm_medium=amp&utm_campaign=speakabl"
economist = "https://www.economist.com/news/finance-and-economics/21735055-china-has-taken-harsh-line-south-korea-contemplates-banning-bitcoin"
teaparty = "https://www.teaparty.org/iraq-war-vet-lost-leg-battle-shuts-david-hogg-brutal-message-298358/"
infowars = "https://www.infowars.com/piers-morgan-asks-where-britain-would-be-without-americas-guns-alex-jones-friend-youd-be-speaking-german/"
pew = "http://www.pewinternet.org/2011/03/17/the-internet-and-political-news-sources/"
buzzfeed = "https://www.buzzfeed.com/michaelblackmon/new-york-city-police-are-investigating-a-scuffle-involving?bfsplash&utm_term=.wqEm1qPZw#.nfxKeO6X7"

def extract_from_tags(soup, tag):
    tags = soup.find_all(tag)
    extracted = []
    for tag in tags:
        for x in tag.descendants:
            if len(x) > 0 and str(type(x)) == "<class 'bs4.element.NavigableString'>":
                extracted.append(x)
    return extracted

# extracter code
def scrape_from_url(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    title = soup.title.string
    # print('title is ', title)

    #get all text in h1s
    h1tags = extract_from_tags(soup, 'h1')
    h1_string = " ".join(h1tags)
    # print('h1s are ', h1_string)

    #cross check title with h1 and only include those that are in both
    title_words = title.split()
    #avoid empty h1s in the list
    h1_words = list(filter( lambda x: len(x) > 0, h1_string.split()))
    h1_words_upper = [word.upper() for word in h1_words]
    #if there are no h1s, just use title, otherwise cross-check
    if len(h1_words) > 0:
        headline = " ".join([word for word in title_words if word.upper() in h1_words_upper])
    else:
        headline = " ".join(title_words)

    #get first paragraph
    ptags = extract_from_tags(soup, 'p')
    first_paragraph = ""
    for p in ptags:
        if '.' in p:
            first_paragraph = p
            break;

    return headline + " " + first_paragraph
# print(scrape_from_url(pew))
