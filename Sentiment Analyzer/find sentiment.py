import re
import string
from textblob import TextBlob

def clean_message(message):
    punc_removed = [char for char in message if char not in string.punctuation]
    return ''.join(punc_removed)
  
def get_message_sentiment(message):
    analysis = TextBlob(clean_message(message))
    
    if analysis.sentiment.polarity > 0.2:
        return 'positive'
    elif analysis.sentiment.polarity > -0.1:
        return 'neutral'
    else:
        return 'negative'

if __name__ == "__main__":
    print(get_message_sentiment("I had so much fun participating in MLH Hackathon this weekend."))