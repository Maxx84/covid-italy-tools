#!/usr/bin/env python
"""
COVID-19 - Italian Data Plotting Tool

This script fetches the latest covid-19 data from Dipartimento della 
Protezione Civile (pcm-dpc) and generates several plots.
"""

import math
import sys
import csv
import urllib2

import matplotlib.pyplot as plt

def fetch_latest_data():
	"""
    use urllib2 to download the latest csv from pcm-dpc's github
    """
	print("Fetching csv file...")

	url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
	raw_data = urllib2.urlopen(url)

	return raw_data


def parse_data(csv_data):

	data = csv.reader(csv_data)

	header = next(data) # gets the first line

	return header, data


def main():
	data = fetch_latest_data()
	header, rows = parse_data(data)


if __name__ == '__main__':
	main()