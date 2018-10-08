#!/usr/bin/env python2

"""
Process text with a NLP (Natural Language Processing) library.

Produces as output a CSV file with the sentiment, and the tweet text.
"""

import argparse
import csv
import glob
import sys

from pattern.en import sentiment

def main():
	# user input
	parser = argparse.ArgumentParser(description='Process tweets found in CSVs in a directory using a NLP library')
	parser.add_argument('--dir', help='Input directory',required=True)
	parser.add_argument('--out', help='Output CSV file name', default='nlp.csv')
	args = parser.parse_args()

	tweets_sentiment = []

	# iterate all csv's produced by collectors
	for csv_file in glob.glob("%s/tweets-collector_*.csv" % args.dir):
		# open csv
		with open(csv_file, "r") as infile:
			reader = csv.reader(infile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
			for row in reader:
				tweet = row[0]
				tweet_sentiment = sentiment(tweet)
				tweets_sentiment.append({'sentiment': tweet_sentiment[0], "text": tweet})

	# write tweets and sentiment to a new csv
	with open(args.out, "w") as outfile:
		writer = csv.writer(outfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
		for row in tweets_sentiment:
			writer.writerow([row['sentiment'], row['text']])

if __name__ == '__main__':
	main()
	sys.exit(0)
