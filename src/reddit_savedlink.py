import praw
import prawcore
import sys
from time import time
import json
from pprint import pprint
from .user import user,pw

DEBUG_MESSAGES = True

def debug_print( msg ) :
    if DEBUG_MESSAGES:
        print(msg)

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
        print("Error logging in.")
        sys.exit(0)
    except:
        print("unrecognized error")
        sys.exit(0)
    return reddit

# limit: max # of links to pull
# count: # of links pulled so far
def getSavedLinksPRAW(redditor, limit, after, count=0):
    print("Getting saved links")
    try:
        if after != None:
            print(after)
            savedLinks = redditor.saved(limit=limit,params={'after':after,'count':count})
        else:
            savedLinks = redditor.saved(limit=limit)
    except prawcore.exceptions.Forbidden:
        print("Error connecting.")
        sys.exit(0)

    print("Got 'em.")
    return savedLinks

# count: # of links to pull at a time
# limit: # of total pulls to perform. Use 0 for unlimited
def getSavedLinks( cmd, count=100, limit=0 ):
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Starting with count %d and limit %d" % (count, limit))

    reddit = connect()

    print("Connected as "),
    redditor = praw.models.Redditor(reddit,user)
    print(redditor)

    reqTime = time()
    print(reqTime)
    savedLinks = getSavedLinksPRAW(redditor, count, None)

    savedLinkOut = []
    if cmd == "list":
        i = 1                                                   # loop index starts at 1 since we already performed a pull
        while True:
            if ( time() - reqTime < 2 ):                        # ratelimit: check to see if enough time has elapsed
                continue                                        # busy-wait until enough time has elapsed

            print(time())

            countRemaining = count
            for link in savedLinks:
                linkdata = vars(link)
                fullname = linkdata["name"]
                # print(fullname + ": "),

                # if fullname[:2] == "t1":
                #     savedLinkOut.append(linkdata["link_title"])
                # elif fullname[:2] == "t3":
                #     savedLinkOut.append(linkdata["title"])

                savedLinkOut.append(linkdata)
                # pprint(linkdata)
                countRemaining -= 1

            print("countRemaining: %d" % countRemaining)

            if ( limit > 0 and i == limit ):
                print("At limit. Breaking.")
                break

            if ( countRemaining > 0 ):                      # if we didn't reach the limit, we're at the end of the content
                # print("%d remaining. Breaking.", countRemaining)
                break

            print("retrieving more...")
            i += 1
            savedLinks = getSavedLinksPRAW(redditor, limit, fullname, i * count)

    elif cmd == "dev":
        linkdata = None
        for link in savedLinks:
            linkdata = vars(link)
            break
        pprint(linkdata["subreddit"])
        pprint(type(linkdata["subreddit"]))

    print("Done.")
    return savedLinkOut
