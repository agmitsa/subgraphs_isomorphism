from pprint import pprint

def adjencymatrix(file):
	filecontents = []
	with open(file) as input_file:
		for line in input_file:
			filecontents.append( line.split() )

	if filecontents[0][0].isalpha():
		for x in range(len(filecontents)):
			filecontents[x] = [ord(filecontents[x][0]) -96 , ord(filecontents[x][1])-96]
	else:
		for x in range(len(filecontents)):
			filecontents[x] = [int(filecontents[x][0]), int(filecontents[x][1])]
	
	max = 0
	for x in filecontents:
		if x[0]>max:
			max = x[0]
		if x[1]>max:
			max = x[1]

	matrix = []
	for x in range(max):
		submatrix=[]
		for y in range(max):
			submatrix.append(0)
		matrix.append(submatrix)

	for x in filecontents:
		matrix[x[0]-1][x[1]-1] = 1
		matrix[x[1]-1][x[0]-1] = 1
		
	return matrix
	
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

def simple_enumeration(A,B,Morg,d):
	global recursions
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
			#j starts zero out all non-zero elements in eth column
			for j in range(len(M)):	
				if j != d:
					M[j][e] = 0

			if d == len(A)-1:
				#pprint(M)
				#print(d, " ", e)
				product = cTable(M, B)
				transpose = transposeTable(product)
				C = cTable(M, transpose)
				
				if C==A:
					print("M:")
					pprint(M)
					print("B:")
					pprint(B)
					print("product:")
					pprint(product)
					print("transpose:")
					pprint(transpose)
					print("C:")
					pprint(C)
					print("A:")
					pprint(A)
					print("\n\n\n")

					return M
			else:
				#print ("d:", d, " e:", e)
				result = simple_enumeration(A,B,M,d+1)
				if result is not None:
					return result

a_matrix, b_matrix = adjencymatrix("C:\\Users\\user\\Desktop\\assignment-2019-4\\graph_1a.txt"), adjencymatrix("C:\\Users\\user\\Desktop\\assignment-2019-4\\graph_3a.txt")
pprint(a_matrix)
print("\n")
pprint(b_matrix)
print("\n")
m_matric = mTable(a_matrix, b_matrix)
pprint(m_matric)
print("\n")
ret = simple_enumeration(a_matrix, b_matrix, m_matric, 0)
print(ret)
print(recursions)