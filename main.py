import praw
import prawcore
from pprint import pprint
import sys
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


# 'connected as ' +
redditor = praw.models.Redditor(reddit,user)
print(redditor)

savedLinks = redditor.saved(limit=3)

for link in savedLinks:
    pprint(vars(link))

# i = 0
# for link in saved:
#     if i > 4:
#         break
#     item = praw.models.Submission(reddit, link)
#     print item.fullname
#     i += 1

debug_print("Done.")
