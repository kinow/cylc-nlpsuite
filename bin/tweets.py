#!/usr/bin/env python2

"""
Downloads tweets using Twitter's API (30 max), and archives them
as CSV.

The user input contains the search word, and the CSV output file
name.
"""

import argparse
from pattern.web import Twitter
import csv
import sys

def main():
	# user input
	parser = argparse.ArgumentParser(description='Downloads tweets for a given search word')
	parser.add_argument('--term', help='Term to search tweets',required=True)
	parser.add_argument('--out', help='Output CSV file name', default='tweets.csv')
	args = parser.parse_args()
	# Twitter engine
	engine = Twitter(language='en')
	with open(args.out, "w") as outfile:
		writer = csv.writer(outfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
		# download tweets
		for tweet in engine.search(args.term, cached = False, start=1, count=30):
			csvrow = [s.encode('utf-8') for s in tweet.values()]
			# write into CSV file
			writer.writerow(csvrow)

if __name__ == '__main__':
	main()
	sys.exit(0)
