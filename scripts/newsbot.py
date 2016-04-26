from sys import argv

script, filename = argv

import csv

with open(filename, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	
	thisIsFirstRow = 1
	
	for inreLista in spamreader:
		if thisIsFirstRow == 0:
			print inreLista[0] + " earns " + inreLista[2] + " euro per month."
		else:
			thisIsFirstRow = 0
