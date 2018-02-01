import time
import json
import tweepy
from tweepy import OAuthHandler
    
from tweepy import Stream
from tweepy.streaming import StreamListener



print "PROCESS STARTED ON : " + time.strftime("%c")

time.sleep(.2)

#GETTING ACCESS DETAILS CREDENTIALS FROM TWITTER API FOR PERSONAL ACCOUNT

print "GETTING ACCESS DETAILS CREDENTIALS FROM TWITTER API FOR PERSONAL ACCOUNT"

time.sleep(.2)

#APP INFO
access_token = "931395532714532864-8UZliQzqPbe2miDJmljPjSr3XpMCydw"
access_token_secret = "LO1hkcXbp0rbEQdwuuC3MFGhKmUIG6NNDjivYzwqvOREQ"

print "Getting App Info..."

time.sleep(.2)


#CONSUMER INFO FOR APP
api_key = "4b8QWsWUfDEG9NPEeS2OQc570"
api_secret = "a4ckajoZv81V5b3rBSjWrJM4Nq7voBxHO7d1kNFWpDOJulp3mf"

print "Getting User Information..."

time.sleep(.2)

#VALIDATION OF CREDENTIALS USIND LATEST OAUTH AUTHORSATION PROTOCOL
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

print "Validating Credentials..."

time.sleep(.2)

# API CREATION USING OAUTH AUTHENTICATION PROTOCOL
api = tweepy.API(auth)

print "Creating API..."

time.sleep(.2)

#GETTING PUBLIC TWEETS FROM USER'S HOME TIMELINE

print "Getting Tweets..."

class MyListener(StreamListener):
 
    def on_data(self, data):
        print "..."
        try:
            with open('tweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['#fun'])

	
print "TWEETS SUCCESFULLY DOWNLOADED IN 'tweet.txt'..."
