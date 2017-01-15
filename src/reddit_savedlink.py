import praw
import prawcore
import sys
from time import time
import json
from pprint import pprint
from user import user,pw

DEBUG_MESSAGES = True

def debug_print( msg ) :
    if DEBUG_MESSAGES:
        print msg

def connect():
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
    return reddit

def getSavedLinksPRAW(redditor, limit, after, count=25):
    print("Getting saved links")
    try:
        if after != None:
            print after
            savedLinks = redditor.saved(limit=limit,params={'after':after,'count':count})
        else:
            savedLinks = redditor.saved(limit=limit)
    except prawcore.exceptions.Forbidden:
        print "Error connecting."
        sys.exit(0)

    print("Got 'em.")
    return savedLinks

def getSavedLinks( cmd ):
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print("Starting...")

    reddit = connect()

    print("Connected as "),
    redditor = praw.models.Redditor(reddit,user)
    print(redditor)

    limit = 100
    reqTime = time()
    print reqTime
    savedLinks = getSavedLinksPRAW(redditor, limit, None)

    savedLinkOut = []
    if cmd == "list":
        i = 0
        while True:
            # ratelimit: check to see if enough time has elapsed
            if ( time() - reqTime < 2 ):
                # busy-wait until enough time has elapsed
                continue

            print time()

            count = limit
            for link in savedLinks:
                linkdata = vars(link)
                fullname = linkdata["name"]
                # print(fullname + ": "),

                if fullname[:2] == "t1":
                    savedLinkOut.append(linkdata["link_title"])
                elif fullname[:2] == "t3":
                    savedLinkOut.append(linkdata["title"])
                # pprint(linkdata)
                count -= 1

            print ("count: %d" % count)

            if ( i == 5 ):
                break

            if ( count > limit ):
                # if we didn't reach the limit, we're at the end of the content
                break

            print "retrieving more..."
            savedLinks = getSavedLinksPRAW(redditor, limit, fullname, count)
            i += 1

    elif cmd == "dev":
        linkdata = None
        for link in savedLinks:
            linkdata = vars(link)
            break
        pprint(linkdata["subreddit"])
        pprint(type(linkdata["subreddit"]))

    print("Done.")
    return savedLinkOut
