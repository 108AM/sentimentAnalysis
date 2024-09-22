import tweepy
import csv

# token for twitter developers
client = tweepy.Client(
    bearer_token="AAAAAAAAAAAAAAAAAAAAAD30lAEAAAAAg28%2FktcJ3e4p1Cd6M0FrJaqKlS8%3DUpNWeqiyQ9P61Hbc8cPQbEmLWprehqxTPy7hADu9lzYhmHPANZ",
    consumer_key="Vbs8xYPYv54YYbXBXb5DDp4ta",
    consumer_secret="7klzAH6aPMDUv67rVYYzoZmxT4rNkKOrjdNgHYOm4VugDHxUoU",
    access_token="1614668549812883457-T63t150POWXiWBbU792hXF6CzJ9rMt",
    access_token_secret="pflLaABss0WasCwxWce3YPD7l5IAvLCGDIuUfUsW736vz",
)

#function which scrapes tweets and writes them to a csv file
def scrapeTweets(input, filename):

    #creates an object of class client whose attribute data contains the required tweets
    response = client.search_recent_tweets(
        
        #the required conditions to be fulfilled by the tweet (language, key terms)
        "%s -is:retweet lang:en" % input,
        max_results = 50,
        tweet_fields = ['author_id','created_at','text','source','lang','geo'],
    )

    #opens csv file and writes each tweet into the file as a new line
    with open(filename, 'a', newline='', encoding='utf-8') as file:

        #creates object whose writerow() method allows it to write lines to the csv
        writer = csv.writer(file)

        try:
        
            for tweet in response.data:

                #only writes to the csv if the tweet is below 280 characters
                if len(tweet.text) < 280 and len(tweet.text)>50:
                    writer.writerow([tweet.text])
        
        except:
            pass

