#!/usr/bin/env python3

import pandas as pd
from sys import argv
from os.path import split, splitext
from sqlalchemy import create_engine


def newName(name):
	newName = ''
	for c in name:
		c2 = ''
		if c == ' ':
			continue
		if str.isupper(c):
			c2 = '_'
		newName = newName + c2 + str.lower(c)

	if newName[0] == '_':
		return newName[1:]	
	return newName


if __name__ == "__main__":
	if len(argv) == 1:
		print('Usage: csc2pg  <full filename> [<tablename>]')
		print("\tExample: csc2pg  customer.csv customer")
		exit(1)


	filename = argv[1]

	if  len(argv) == 2:
		tablename = split(filename)
		tablename = tablename[1]
		tablename = splitext(tablename)
		tablename = tablename[0]
		if tablename == '':
			tablename = tablename[0]

	else:
		tablename = argv[2]


	engine = create_engine('postgresql://postgres:@localhost:5432/test')
	df=pd.read_csv(filename, delimiter=';')


	df = df.rename(columns=lambda x : newName(x) )

	print(df.head())

	df.to_sql(tablename, engine)
