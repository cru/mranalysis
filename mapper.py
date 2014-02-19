#!/usr/bin/env python

import json
import sys

dataFile = open('data/wide_data.json')
rc = 2

for line in dataFile:
#for line in sys.stdin:
    try:

        record = json.loads(line)
        data = record[1]
        mc = len(data)
        # key: position in nxn matrix
        # value: row
        totalExpression = 0
        for j in data:
            totalExpression += int(j)
        mean = float(totalExpression)/len(data)
        
        for i in range(rc+1):
            for j in range(mc+1):
                print "(%s,%s)\t(%s,%s,%s,%s)" % (record[0], j+1, "'a'", record[0], j+1, int(record[1][j]) )
                print "(%s,%s)\t(%s,%s,%s,%s)" % (j+1, record[0], "'b'", j+1, record[0], int(record[1][j]) )

    except:
        pass
        