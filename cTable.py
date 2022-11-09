
def cTable(M, H):
	
	C = []
	
	for x in range(len(M)):
		
		C.append([])
		for y in range(len(H)):		
			sum = 0
			for k in range(len(H)):#len(H)=len(H[y]) αφου Η τετραγωνικος
				sum = sum + M[x][k]*H[k][y]
	
			C[x].append(sum)
			
	return C
	
M = [[0,1,0],
	[1,0,0],
	[0,0,1]]
H = [[0,1,0],
	[1,0,1],
	[0,0,1]]
	
print(cTable(M,H))