import re
import csv
import json
import sys
import requests
from requests.auth import HTTPBasicAuth
import hashlib
'''
	Usage: 'python3 mysqlToJson.py <targetFile.sql>
	
	About:
	Parses an '.sql' file from mysqldump and converts it to JSON for elastic or other document DBS. 
  
	The mysqlFileToArray function parses the sql file into into python objects & arrays, which can be converted into JSON with json.dumps(arrayOfObjects)

	Each resulting object represents a row from a table in the original SQL. 

	mysqlFileToArray adds the fields 'sqltojson_table_name' and 'sqltojson_source_file' to each document. keep or delete them as you wish, ie.
	 		del(document['sqltojson_table_name'])
			del(document['sqltojson_source_file'])
'''

# The brains of the operation
def mysqlFileToArray(sqlFile):
	tac = dict()
	tmpDb = []
	currentTable = ''
	inTableStructure = False

	# 
	for line in open(sqlFile, "r"):

		# 
		if re.search('^CREATE TABLE `\S.+`', line) != None:
			inTableStructure = True
			currentTable = re.search('^CREATE TABLE `\S.+`', line).group(0).replace('CREATE TABLE ', '').replace('`', '')
			tac[currentTable] = []
			continue

		# 
		if inTableStructure:
			# 
			if line.find('PRIMARY KEY') > -1 or line.find(' KEY `') > -1:
				continue

			# Create a map of each table name and it's associated columns. Each column name is preceeded by two spaces
			if re.search('^\ \ `\S.+`', line) != None:
				columnName = re.search('^\ \ `\S.+`', line).group(0).strip().replace('`', '')
				tac[currentTable].append(columnName)

			# This tells us that we are no longer in table description
			if re.search('^\)', line) != None:
				inTableStructure = False
				continue

		# 
		if re.search('^INSERT INTO `' + currentTable + '` VALUES', line) != None:
			line = line[line.find("("):]
			entriesArray = line.split("),(")

			# Remove the semicolon at the end of the last entry
			if (entriesArray[-1][-1] == ';'):
				entriesArray[-1] = entriesArray[-1][:-1]

			# iterate through the table rows
			for entry in entriesArray:
				entry = entry[1:] # Remove the leading ( 
				try:
					tmp = dict()
					# Carve apart the row with the CSV parser
					cvp = list(csv.reader([entry], quotechar="'", delimiter=',', escapechar='\\'))[0]

					# Create 
					for x in range(0, len(cvp)):
						columnName = tac[currentTable][x]
						tmp[columnName] = cvp[x]

					tmp['sqltojson_table_name'] = currentTable.replace(");", "")
					tmp['sqltojson_source_file'] = sqlFile

					tmpDb.append(tmp)
					del(tmp)

				except Exception as e:
					print("Exception in line-49 loop: " + str(e))

	
	# Now take it all and convert it to JSON
	return tmpDb

# Takes in the array from sqlFileToArray, then converts each document in it to JSON and posts it to elastic
def sample_postToElastic(document):
	indexName = ""
	headers = {
		'Content-Type': 'application/json'
	}
	# Choose your own adventure: you pick what index the data goes into. I'm recreating the speration of tables here
	indexName = document['sqltojson_table_name']

	# Helps avoid duplicate entries, especially if you run the job multiple times
	s = hashlib.sha1()
	s.update(json.dumps(document).encode('utf-8'))
	docId = s.hexdigest()

	# Posts the document to an index with the same name as the original table
	resp = requests.post('http://127.0.0.1:9200/' + indexName + '/_doc/' + str(docId), auth = HTTPBasicAuth('username', 'password'), headers = headers, data = json.dumps(document))
	if(resp.status_code != 200 and resp.status_code != 201):
		# Something went wrong
		print("Elastic returned non-successful response")
		print(resp.__dict__)
		exit(-1)


if len(sys.argv) < 2:
	print("Usage: python3 mysqlToJson.py <targetFile.sql>")
	exit(0)

# Convert the sql file to an array of JSON documents. Each will have an added 'sqltojson_table_name' field to identify which "table" it belongs to
convertedDb = mysqlFileToArray(sys.argv[1])

# Add each document to elastic. modify the sample_postToElastic to fit your needs
for document in convertedDb:
	'''
	# Modify the object as you wish here, ie add an '_id' field
	s = hashlib.sha1()
	s.update(json.dumps(document).encode('utf-8'))
	document['_id'] = s.hexdigest()
	'''

	# Prints out the converted document
	print(json.dumps(document))

  	# Add the document to your db
	# sample_postToElastic(document)
	# Modify sample_postToElastic for your elastic stack, or use it as guide for other NoSQL document DBs 

