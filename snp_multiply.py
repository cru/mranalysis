import MapReduce
import sys

"""
Matrix Multiply Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

n = open(sys.argv[1]) 
lc = 0
for line in n:
	lc += 1

def mapper(record):
	# key: position in nxn matrix
	# value: row
	sum = 0
	for j in record[1]:
		sum += int(j)
	mean = float(sum)/len(record[1])
	for i in range(1, lc+1):
		for j in range(len(record[1])):
			mr.emit_intermediate((record[0], i), ("a", record[0], j, int(record[1][j]) - mean))
			mr.emit_intermediate((i, record[0]), ("b", j, record[0], int(record[1][j]) - mean))

def reducer(key, list_of_values):
	# key: position on nxn matrix
	# value: list of records that may have an effect on the position
	sum = 0
	a = []
	b = []
	for record in list_of_values:
		a.append(record) if record[0] == 'a' else b.append(record)
	for ra in a:
		for rb in b:
			if ra[2] == rb[1]:
				sum += int(ra[3]) * int(rb[3]); 
	mr.emit((key[0], key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	mr.execute(inputdata, mapper, reducer)
