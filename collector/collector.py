import twitter, json, StringIO
from textblob import TextBlob
                      
def main():
    api = twitter.Api(consumer_key='xiRvwM5u5lgLW4GsfMq1BLxmw',
                  consumer_secret='A7IPWnxsfTfTccnuyF9TXPXEBwpC6WyEVwkNseJXxv4SVqhncd',
                  access_token_key='1939224967-lZqH7LpKSs775MCNK2ynZlJ0meUIcDt9QiM5KAt',
                  access_token_secret='bgelSzudLaRrKaQcIHvXOXvNW7QaoNpEiaLmnGAnvYNmt')
    valueswecareabout = []
    query = api.GetSearch(term="adele", count = 100,geocode = ("38.5000","98.0000","3000km"))
    for status in query:
        valueswecareabout.append((status.text, status.location, status.coordinates, status.geo, status.place))
    for tweet in valueswecareabout:
        print getSentiment(tweet[0])

def getSentiment(tweet):

		value = TextBlob(tweet)
		return value.sentiment.polarity
        
if __name__=='__main__':
    main()
