#!/usr/bin/env python

import json
import sys

dataFile = open('data/wide_data.json')

lc = 0
for line in dataFile:
    lc += 1
print lc

#for line in sys.stdin:
for line in dataFile:
    record = json.loads(line)
    data = record[1]
    mc = len(data+1)
    print mc
    totalExpression = 0
    for j in data:
        totalExpression += int(j)
    mean = float(totalExpression)/len(data)
    
    for i in range(1,lc):
        print i
        for j in range(1,mc):
            print j
            # print "(%s,%s)\t(%s,%s,%s,%s)" % (record[0], i, "'a'", record[0], j+1, int(record[1][j]) )
            # print "(%s,%s)\t(%s,%s,%s,%s)" % (i, record[0], "'b'", j+1, record[0], int(record[1][j]) )

        