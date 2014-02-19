#!/usr/bin/env python

import json
import sys

file = open('data/wide_data.json')
for line in file:
#for line in sys.stdin:
    try:
        record = json.loads(line)
        id = record[0]
        data = record[1]
        lc = len(data)
        # key: position in nxn matrix
        # value: row
        totalExpression = 0
        for j in data:
            totalExpression += int(j)
        #print totalExpression
        mean = float(totalExpression)/len(data)
        print mean
        for i in range(1, lc+1):
            for j in range(len(record[1])):
                print "%s\t%s\t%s\t%s\t%s\t%s" % (record[0], i, "a", record[0], j, str(int(record[1][j]) - mean))
                print "%s\t%s\t%s\t%s\t%s\t%s" % (i, record[0], "b", j, record[0], str(int(record[1][j]) - mean))

    except:
        pass
        