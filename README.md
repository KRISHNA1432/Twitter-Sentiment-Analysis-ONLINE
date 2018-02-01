

# Twitter-Sentiment-Analysis-ONLINE
Download And Analyse the tweets to predict their sentiment i.e. EMOTIONS

AFFINN File is already  given by the researchers

STEPS : 

1.  establish a connection with good bandwidth
2.  install python interpreter compatibility software.
3.   run download.py to download tweets
4.   run newterm.py
5.  run total.py

Details : 

What is sentiment analysis?
Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker.

Authentication:
In order to fetch tweets through Twitter API, one needs to register an App through their twitter account. Follow these steps for the same:

1.  Open this link and click the button: ‘Create New App’
2.  Fill the application details. You can leave the callback url field empty.
3.  Once the app is created, you will be redirected to the app page.
4.  Open the ‘Keys and Access Tokens’ tab.
5.  Copy ‘Consumer Key’, ‘Consumer Secret’, ‘Access token’ and ‘Access Token Secret’.

We follow these 3 major steps in our program:
Authorize twitter API client.
Make a GET request to Twitter API to fetch tweets for a particular query.
Parse the tweets. Classify each tweet as positive, negative or neutral.

WORKING :

if analysis.sentiment.polarity > 0:
       return 'positive'
elif analysis.sentiment.polarity == 0:
       return 'neutral'
else:
       return 'negative'
