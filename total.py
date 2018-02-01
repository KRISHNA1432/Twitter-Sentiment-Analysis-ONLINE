import sys
import json

def main():                                     #CREATING DATA STRUCTURES
  words = open(sys.argv[1])
  tweets = open(sys.argv[2])	
  scores = {}
  tweet_text = []

  for WORD in words:
    term, score = WORD.split("\t")
    scores[term] = int(score)
    
  for line in tweets:
    tweet = json.loads(line)
    if 'text' in tweet:
      text = tweet['text'].lower()
      tweet_text.append(text.encode('utf-8'))

    for t in tweet_text:
      sentiment = 0
      breakdown = t.split()
    
      for word in breakdown:
        if scores.has_key(word):
          sentiment = sentiment + scores[word]

        if sentiment > 0 :
          SENT = 'POSITIVE'
        if sentiment < 0 :
          SENT = 'POSITIVE '
        if sentiment == 0 :
          SENT = 'NEUTRAL'
      
      print(t , "----------->", sentiment,"-------------->",SENT)

if __name__ == '__main__':
    main()
