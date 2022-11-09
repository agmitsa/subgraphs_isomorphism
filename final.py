from pprint import pprint

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
	
def cTable(M, H):
	
	C = []
	
	for x in range(len(M)):
		
		C.append([])
		for y in range(len(H[0])):		
			sum = 0
			for k in range(len(H)):
				sum = sum + M[x][k]*H[k][y]
	
			C[x].append(sum)
			
	return C

def mTable(A, B):

	m = [[0 for x in range(len(B))] for y in range(len(A))]

	adegree = 0
	bdegree = 0
		
	for i in range(len(A)):
		adegree = sum(A[i])
		for j in range(len(B)):
			bdegree = sum(B[j])
			if bdegree >= adegree:
				m[i][j] = 1
			
	return m		

def transposeTable(T):
	transpose = [[0 for x in range(len(T))] for y in range(len(T[0]))]
	for i in range(len(transpose)):
		for j in range(len(transpose[0])):
			transpose[i][j] = T[j][i]
	return transpose

recursions = 0
output = None

def simple_enumeration(A,B,Morg,d):
	global recursions,output
	recursions+=1

	if d >= len(A):
		return None

	#e is for each element in the dth row of M	
	for e in range(len(Morg[d])):
		if Morg[d][e] != 0:

			M = [[i for i in row] for row in Morg]
		
			#k starts zero out all non-zero elements in the eth row
			for k in range(len(M[d])):
				if k != e:
					M[d][k] = 0		
			for j in range(len(M)):
				if j != d:
					M[j][e] = 0						
			if d == len(A)-1:
				product = cTable(M, B)
				transpose = transposeTable(product)
				C = cTable(M, transpose)
				
				if C==A:
					output=M
			else:
				simple_enumeration(A,B,M,d+1)
				
	return output
				
def are_neighbours_mapped(A,B,M,i,j):
	for k in range(len(A)):
		if A[i][k] != 0:
			found = False
			for l in range(len(B)):
				if B[j][l] != 0:
					if M[k][l] != 0:
						found = True
			if found == False:
				return False
	return True

def refine(A,B,M):
	done = False
	while not done:
		done = True
		for i in range(len(M)):
			rs = 0
			for j in range(len(M[0])):
				if M[i][j] != 0:
					if are_neighbours_mapped(A,B,M,i,j) == False:
						M[i][j] = 0
						done = False
					else:
						rs = rs + 1
			if rs == 0:
				return False
	return True

def refined_enumeration(A,B,Morg,d):
	global recursions,output
	recursions+=1

	if d >= len(A):
		return None

	#e is for each element in the dth row of M	
	for e in range(len(Morg[d])):
		if Morg[d][e] != 0:

			M = [[i for i in row] for row in Morg]
		
			#k starts zero out all non-zero elements in the eth row
			for k in range(len(M[d])):
				if k != e:
					M[d][k] = 0		
			for j in range(len(M)):
				if j != d:
					M[j][e] = 0

			proceed = refine(A,B,M)
			if proceed == True:
				if d == len(A)-1:
					product = cTable(M, B)
					transpose = transposeTable(product)
					C = cTable(M, transpose)
					
					if C==A:
						output=M
				else:
					refined_enumeration(A,B,M,d+1)
				
	return output


a_matrix, c1 = adjencymatrix("C:\\Users\\user\\Desktop\\assignment-2019-4\\graph_4.txt")
b_matrix, c2 = adjencymatrix("C:\\Users\\user\\Desktop\\assignment-2019-4\\graph_5.txt")
m_matric = mTable(a_matrix, b_matrix)
ret = simple_enumeration(a_matrix, b_matrix, m_matric, 0)

for i in range(len(ret)):
	for j in range(len(ret[i])):
		if ret[i][j]==1:
			print(c1[i][1],'->', c2[j][1])
			
print(recursions)
