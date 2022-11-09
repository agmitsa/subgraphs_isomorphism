def transposeTable(T):
	transpose = [[0 for x in range(len(T))] for y in range(len(T[0]))]
	for i in range(len(transpose)):
		for j in range(len(transpose[0])):
			transpose[i][j] = T[j][i]
	return transpose


M = [[0,1,0],
	[1,0,0],
	[0,0,1],
	[2,3,4]]

print(M)
print("\n")
print(transposeTable(M))