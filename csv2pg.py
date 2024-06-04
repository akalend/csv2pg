#!/usr/bin/env python3

from sys import argv
from os.path import split, splitext
from sqlalchemy import create_engine
import pandas as pd


def newName(name):
    newName = ''
    pred = ' ';
    for c in name:
        c2 = ''
        if c == ' ':
            continue
        if c == '_' and pred == '_':
            continue;
        if str.isupper(c):
            if pred != '_' and pred != '-':
                c2 = '_'
            pred = '_'

        newName = newName + c2 + str.lower(c)
        pred = c

    pred = newName[-1];

    if newName[0] == '_':
        return newName[1:]

    return newName


if __name__ == "__main__":
    if len(argv) == 1:
        print('Usage: csc2pg  <full filename> [<tablename>] [<schema>]')
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



    database = 'postgres'
    if len(argv) == 4:
        database = argv[3]

    engine = create_engine('postgresql://postgres:@localhost:5432/' + database)
    # engine = create_engine('postgresql://postgres:@127.0.0.1:5433/postgresml')
    df=pd.read_csv(filename, delimiter=',')
    print(df.columns)

    df = df.rename(columns=lambda x : newName(x))
    

    if len(argv) == 4:
        print("tablename={}  dbname={}".format(tablename, argv[3]))
    else:
        print("tablename={} ".format(tablename))

    df.to_sql(tablename, engine)
    # df.to_sql(tablename, engine, schema = argv[3])