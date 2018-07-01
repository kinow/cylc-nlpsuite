#!/usr/bin/env python2

"""
Post-process step that removes negative tweets.

The output is a new CSV file with the text and sentiment. The
tweets are ordered according to the length of the text.
"""

import argparse
import csv
import glob
import sys

from pattern.en import sentiment

def main():
	parser = argparse.ArgumentParser(description='Post-process to remove negative tweets')
	parser.add_argument('--file', help='NLP CSV',required=True)
	parser.add_argument('--out', help='Output CSV file name', default='final.csv')
	args = parser.parse_args()

	with open(args.out, "w") as outfile:
		writer = csv.writer(outfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
		with open(args.file, "r") as infile:
			reader = csv.reader(infile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
			for row in reader:
				tweet_sentiment = row[0]
				if tweet_sentiment > 0:
					text = row[1]
					writer.writerow([text])

if __name__ == '__main__':
	main()
	sys.exit(0)

