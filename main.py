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
print("Starting...")

cmd = "list"

argc = len(sys.argv)
if argc == 2:
    cmd = sys.argv[1]
elif argc > 2:
    print("usage: python main.py <cmd>")
    sys.exit(0)

print("Connecting to Reddit...")
try:
    reddit = praw.Reddit(client_id='rsHOJ-vVYdLZuw',
                     client_secret='BUa8NPGly-juAhsiTn3BYgZJ8jw',
                     password=pw,
                     user_agent='testscript by /u/tom---swift',
                     username=user)
    # print(reddit.user.me())
except prawcore.exceptions.Forbidden:
    print "Error logging in."
    sys.exit(0)
except:
    print "unrecognized error"
    sys.exit(0)

print("Connected as "),
redditor = praw.models.Redditor(reddit,user)
print(redditor)

print("Getting saved links")
savedLinks = redditor.saved()
print("Got 'em.")

if cmd == "list":
    for link in savedLinks:
        linkdata = vars(link)
        print(linkdata["name"] + ": "),

        if linkdata["name"][:2] == "t1":
            pprint(linkdata["link_title"].encode("utf-8"))
        elif linkdata["name"][:2] == "t3":
            pprint(linkdata["title"].encode("utf-8"))
elif cmd == "dev":
    linkdata = None
    for link in savedLinks:
        linkdata = vars(link)
        break
    pprint(linkdata["subreddit"])
    pprint(type(linkdata["subreddit"]))
print("Done.")
