import praw
import prawcore
import sys
import json
from pprint import pprint
from user import user,pw

DEBUG_MESSAGES = True

def debug_print( msg ) :
    if DEBUG_MESSAGES:
        print msg

print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
debug_print("Starting...")

try:
    reddit = praw.Reddit(client_id='rsHOJ-vVYdLZuw',
                     client_secret='BUa8NPGly-juAhsiTn3BYgZJ8jw',
                     password=pw,
                     user_agent='testscript by /u/tom---swift',
                     username=user)
    print(reddit.user.me())
except prawcore.exceptions.Forbidden:
    print "Error logging in."
    sys.exit(0)
except:
    print "unrecognized error"
    sys.exit(0)

redditor = praw.models.Redditor(reddit,user)
print(redditor)

savedLinks = redditor.saved()

for link in savedLinks:
    linkdata = vars(link)
    print(linkdata["name"] + ": "),

    if linkdata["name"][:2] == "t1":
        pprint(linkdata["link_title"].encode("utf-8"))
    elif linkdata["name"][:2] == "t3":
        pprint(linkdata["title"].encode("utf-8"))

debug_print("Done.")
