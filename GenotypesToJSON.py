mydatabase = "CRCGenotypes.db"
connection = sqlite3.connect(mydatabase)
cursor = connection.cursor()
query = ''' select barcode, genotype from Genotypes'''
cursor.execute(query)

with open('Genotypes.json', 'w') as f:
	for row in cursor.fetchone():
		f.write(row + '\n')
