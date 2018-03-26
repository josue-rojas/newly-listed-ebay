import webbrowser
from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_ipg=50%27&_nkw=yeezy+boost+350+v2&_sop=10'

#i use a set to keep track of the urls (ebay urls sometimes change so i think its best to keep the whole url)
seen = set([])

# returns list of <a class='vip'></a>
def getLinks():
    r = requests.get(url).content
    soup = BeautifulSoup(r)
    return soup.find_all('a', {'class':'vip'})



def main():
    for link in getLinks():
        itm_link = link.get('href')
        if not itm_link in seen:
            seen.add(itm_link)
            print(itm_link)
    while(True):
        time.sleep(60)
        print('Checking....')
        for link in getLinks():
            itm_link = link.get('href')
            if not itm_link in seen:
                print(itm_link)
                webbrowser.open(itm_link)
                seen.add(itm_link)
            else:
                print('None found...')
                break


if __name__ == "__main__":
    main()
