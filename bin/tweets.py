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
import os
import errno

def mkdir_p(path):
    """https://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python"""
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def main():
    # user input
    parser = argparse.ArgumentParser(description='Downloads tweets for a given search word')
    parser.add_argument('--term', help='Term to search tweets',required=True)
    parser.add_argument('--out', help='Output CSV file name', default='tweets.csv')
    args = parser.parse_args()
    # Twitter engine
    engine = Twitter(language='en')
    term = " ".join(args.term.split("_"))
    mkdir_p(os.path.dirname(args.out))
    with open(args.out, "w") as outfile:
    	print("Searching for tweets with '{}'".format(term))
        writer = csv.writer(outfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
        # download tweets
        for tweet in engine.search(term, cached = False, start=1, count=30):
            csvrow = tweet.text.encode('utf-8')
            # write into CSV file
            writer.writerow([csvrow])

if __name__ == '__main__':
    main()
    sys.exit(0)
