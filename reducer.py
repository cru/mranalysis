#!/usr/bin/env python

import sys
    
# key: position on nxn matrix
# value: list of records that may have an effect on the position
a = []
b = []
cellSum = 0
for line in sys.stdin:
    record = line.strip().split("\t")
    key = eval(record[0])
    rec = eval(record[1])
    a.append(rec) if rec[0] == 'a' else b.append(rec)

    
for row in a:
    for col in b:
    
        if row[1] == col[2]:
            cellSum += row[3]*col[3]
    print cellSum
    #         cellSum += row[3] * col[3]; 
    # print '%s\t%s\t%s' % (str(key[0]), str(key[1]), str(cellSum)) 

    
    #print '%s\t%s\t%s' % (key[0],key[1], str(cellSum))