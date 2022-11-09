from pprint import pprint
from collections import Counter
import itertools

def adjencymatrix(file):
	filecontents = []
	with open(file) as input_file:
		for line in input_file:
			filecontents.append( line.split() )
			
	count = []
	for x in range(len(filecontents)):
		for y in range(len(filecontents[x])):
			if filecontents[x][y] not in count:
				count.append(filecontents[x][y])
	
	counter_list = list(enumerate(count))

	matrix = []
	for x in range(len(count)):
		submatrix=[]
		for y in range(len(count)):
			submatrix.append(0)
		matrix.append(submatrix)
		
	
	for c1, e1 in counter_list:
		for c2,e2 in counter_list:
			if[e1,e2] in filecontents:
				matrix[c1][c2] = 1
				matrix[c2][c1] = 1	
				
	del count		
	return matrix, counter_list
			
	
matrixa, c1 = adjencymatrix("C:\\Users\\user\\Desktop\\assignment-2019-4\\graph_4.txt")
matrixb, c2 = adjencymatrix("C:\\Users\\user\\Desktop\\assignment-2019-4\\graph_5.txt")

pprint(matrixa)
print(c1)
pprint(matrixb)
print(c2)
