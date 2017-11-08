import tweepy
from textblob import TextBlob
consumer_key = "aSCiLsaBYxbIk9HuhiV6Kj980"
consumer_secret = "cYBUulcqMhvzGVdR5diA20OsjwsNkn0QZ4tvBjpGUEIeOhsD2u"

access_token = "855084718114648064-mc9Jwhe6d4T6ekBD8YbkU7hJkFhTSdF"
access_token_secret = "EFn5INTzrDxLMfcxQT74WQwt2hGeOGCuUnW4QlMG8qU6q"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

while True:
    print("Search for tweets on Twitter!")
    print("Only characters are allowed!")
    searchWord = input("Search word: ")
    public_tweets = api.search(searchWord)

    numberOfTweets = 0
    polarity = 0
    subjectivity = 0

    for tweet in public_tweets:
        print(tweet.text, "\n")
        analysis = TextBlob(tweet.text)
        numberOfTweets = numberOfTweets + 1
        polarity += analysis.polarity
        subjectivity += analysis.subjectivity
        #print(analysis.sentiment, "\n")

    print("Calculating average result.. \n")
    avg_polarity = polarity/numberOfTweets
    avg_subjectivity = subjectivity/numberOfTweets
    print("Total number of tweets read: ", numberOfTweets)
    print("Average polarity", avg_polarity)
    print("Average subjectivity", avg_subjectivity)
    print("\n")
