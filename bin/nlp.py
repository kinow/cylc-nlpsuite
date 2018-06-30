#!/usr/bin/env python2

"""
Process text with a NLP (Natural Language Processing) library.

Produces as output a CSV file with the sentiment, and the tweet text.
"""

import argparse
from pattern.en import sentiment
import csv
import sys

def main():
	# user input
	parser = argparse.ArgumentParser(description='Process tweets with a NLP library')
	parser.add_argument('--file', help='Input file',required=True)
	parser.add_argument('--out', help='Output CSV file name', default='nlp.csv')
	args = parser.parse_args()

	tweets_sentiment = []

	# open csv
	with open(args.file, "r") as infile:
		reader = csv.reader(infile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			tweet = row[4]
			tweet_sentiment = sentiment(tweet)
			tweets_sentiment.append({'sentiment': tweet_sentiment[0], "text": tweet})

	# write tweets and sentiment to a new csv
	with open(args.out, "w") as outfile:
		writer = csv.writer(outfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
		for row in tweets_sentiment:
			writer.writerow([row['sentiment'], row['text']])

if __name__ == '__main__':
	main()
	sys.exit(0)
