# FOR ENCOUNTERING FUTURE VERSION CHANGES (HERE, FOR FLOATING POINT VALUES

from __future__ import division

import sys
import json
	
def main():
	words = open(sys.argv[1]) #afinn file
	tweets = open(sys.argv[2]) #output file
	word_scores = {}
	tweet_scores = {}
	tweet_text = []
	new_words = []


	# CREATING HASH TABLE OF WORDS FROM AFINN FILE
	for word in words:
		term, score = word.split("\t")
		word_scores[term] = int(score)


	# LOADING TEXT PART OF TWEET INTO LINE
	for line in tweets:
		tweet = json.loads(line)
		if 'text' in tweet:
			text = tweet['text'].lower()
			tweet_text.append(text.encode('utf-8'))


	# ITERATING THROUGH ALL TWEET'S TEXT PART
	for t in tweet_text:
		sentiment = 0                           # INITIALISING TWEETS SENTIMENT TO 0
		breakdown = t.split()                   # GETTING TWEETS ONE BY ONE
		
		# FOR EVERY WORD IN EACH TWEET
		for word in breakdown:

			if word in word_scores:                                 # WORD FOUND IN DICTIONARY
				sentiment = sentiment + word_scores[word]       
			else:                                                   # LIST OF NEW WORD
				new_words.append(word)

		tweet_scores[t] = int(sentiment)                                # DICTIONARY OF TWEET SCORES


	# CALCULATING SENTIMENT SCORE OF NEW WORD
	for new_word in new_words:
		pos = neg = tot = 0
		for t in tweet_scores:
			if new_word in t:
				if tweet_scores[t] > 0:
					pos+=1
				elif tweet_scores[t] < 0:
					neg+=1
				tot+=1
		SCORE = (pos - neg)/tot
		if SCORE > 0 :
			SENT = 'POSITIVE'
		if SCORE < 0 :
			SENT = 'POSITIVE '
		if SCORE == 0 :
			SENT = 'NEUTRAL'
		print (new_word, "                              ", SENT)

if __name__ == '__main__':
	main()
