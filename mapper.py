#!/usr/bin/env python

import json
import sys

dataFile = open('data/wide_data.json')
rc = 2

for line in dataFile:
#for line in sys.stdin:

    record = json.loads(line)
    data = record[1]
    mc = len(data)
    # key: position in nxn matrix
    # value: row
    totalExpression = 0
    for j in data:
        totalExpression += int(j)
    mean = float(totalExpression)/len(data)
    for i in range(1, rc+1):
        for j in range(0, mc):
            print "(%s,%s)\t(%s,%s,%s,%s)" % (record[0], i, "'a'", record[0], j+1, int(record[1][j]) )
            print "(%s,%s)\t(%s,%s,%s,%s)" % (i, record[0], "'b'", j+1, record[0], int(record[1][j]) )

        