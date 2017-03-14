import tweepy
import csv
import numpy as np
from textblob import TextBlob
from keras.models import Sequential
from keras.layers import Dense

consumer_key= 'Bm5Lh28ztGtPj77lZwwqtAxdV'
consumer_secret= 'zazc4Lo4Nj4k8PmachCiTJzHZodkAyiHfJ8DNrCIDtIvfsog67'
access_token='824895181849636864-AyidUzEL3bYHE5QATJsfrsmwnDz83kb'
access_token_secret='KfmWcwyj0OYLxhV95k9Sngr4ja02Wnuuk1i4eIRNcQBkr'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


public_tweets = api.search('AAPL')

for tweet in public_tweets:    
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    


dates = []
prices = []
def get_data("/Users/Renn 1/Desktop/aapl.csv"):
	with open("/Users/Renn 1/Desktop/aapl.csv", 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader)
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))
	return


get_data('aapl.csv')


def predict_prices(dates, prices, x):

predicted_price = predict_price(dates, prices, 29)
print(predicted_price)