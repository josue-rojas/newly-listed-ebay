# new-ebay-items
A script that constantly checks for new items (provided by a url for now)

### Python needs
- tested in python 3 and 2.7
- beautifulsoup4
- requests
- [terminal-notifier](https://github.com/julienXX/terminal-notifier)
- mac cause of notifier.....

### Usage:
```bash
###########
# DEFAULTS
# url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_ipg=50%27&_nkw=yeezy+boost+350+v2&_sop=10'
# phone_num = ''
# sleep_time = 60
# message = False
# open_links = False
# also defaults always notifies, might disable this later and make it an option....
###########
# -m --message: flag to allow send message of new founding
# -p --phone: phone number to send the message (you can also change defaults in python file instead)(this does not turn on messages, you still need -m)
# -u --url: ebay url of new listings (it is much easier to change default in py file (also make sure url is for new listings))
# -s --sleep: change default sleep time, default is 60sec (or change in py file)


# run script with defaults (changed defaults in py file)
python script.py

# run script w/ defaults and open links automatically
python script.py -o

# run script with phone number messages and different phone from default (w/ default url)
python script.py -m -p 1234567890

# run script with different url (no messages)
python -u  https:\/\/www.ebay.com\/sch\/i.html?_from=R40\&_sacat=0\&_ipg=50%27\&_nkw=yeezy+boost+350+v2\&_sop=10

# run python with different sleep_time (everything else is default)
python -s 30
```

#### Things used (credit & cool things)
- [AppleScript to send messages (only tested with imessage)](https://stackoverflow.com/questions/11812184/how-to-send-an-imessage-text-with-applescript-only-in-provided-service/19483011#19483011)
- [terminal-notifier](https://github.com/julienXX/terminal-notifier), I used this instead of applescript cause it can handle click links

#### TODO
- http://www.helios825.org/url-parameters.php ADD SUPPORT FOR CUSTOM URL IN INPUT
- maybe change to use the ebay api instead!?!?! [here](https://developer.ebay.com/Devzone/finding/CallRef/findItemsAdvanced.html)(but then it would need keys)
