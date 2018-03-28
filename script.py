import webbrowser
from bs4 import BeautifulSoup
import requests
import time
import os
import getopt
import sys

#i use a set to keep track of the urls (ebay urls sometimes change so i think its best to keep the whole url)
seen = set([])

# returns list of <a class='vip'></a>
def getLinks(url):
    r = requests.get(url).content
    soup = BeautifulSoup(r)
    return soup.find_all('a', {'class':'vip'})


def newListing(url, message, phone_num, sleep_time, open_links):
    while(True):
        time.sleep(sleep_time)
        print('Checking....')
        for link in getLinks(url):
            itm_link = link.get('href')
            if not itm_link in seen:
                print(itm_link)
                seen.add(itm_link)
                os.system("terminal-notifier -title 'New Item Found' -message 'Open " + itm_link + "' -open '" + itm_link + "'")
                if open_links:
                    webbrowser.open(itm_link)
                if message:
                    os.system('osascript message.scpt '+ phone_num + ' "' + itm_link +'"')
            else:
                print('No more found...')
                break

def usage():
    print('Usage:\n-m --message: flag to allow send message of new founding\n-p --phone: phone number to send the message (you can also change defaults in python file instead)\n-u --url: ebay url of new listings (it is much easier to change default in py file (also make sure url is for new listings))\n-s --sleep: change default sleep time, default is 60sec (or change in py file)\n-o --open: set open_links to true to automatically open links')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hmp:u:s:o', ['help', 'message','phone=', 'url=', 'sleep=', 'open'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    # ***************************
    # defaults, change them to your liking or use the command line
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_ipg=50%27&_nkw=yeezy+boost+350+v2&_sop=10'
    phone_num = ''
    sleep_time = 60
    message = False
    open_links = False

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            exit()
        elif o in ('-m', '-message'):
            message = True
        elif o in ('-p', '-phone'):
            phone_num = a
        # url is better to change default in this file rather than have an INPUT
        # else you have to escape the characters that interfere like '\' or '&'
        elif o in ('-u', '-url'):
            url = a
        elif o in ('-s', '-sleep'):
            sleep_time = a
        elif o in ('-o', '--open'):
            open_links = True
        else:
            print 'unhandled option'

    # first run should be ignored (i mean unless you want to be notified of a bunch of stuff)
    for link in getLinks(url):
        itm_link = link.get('href')
        if not itm_link in seen:
            seen.add(itm_link)
            print(itm_link)
    # while
    newListing(url, message, phone_num, sleep_time, open_links);


if __name__ == "__main__":
    main()
