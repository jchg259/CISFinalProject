import numpy as np

from matrices import matrices_reader

'''
sequence1 = "GAVLIMXCST"
sequence2 = "GAV-YZXC--"



matrix = np.loadtxt("MatricesTest/Test20.txt", dtype=str)
#print(matrix)

n = len(sequence1)
m = len(sequence2)

pamscore = 0
row = 0
col = 0

for i in range(0,max(n,m)):
	a=0
	b=0
	
	for j in range(0,23):
		if sequence1[i] != matrix[0][a]:
			a = a+1
		else:
			col = a
			#print(col)
			break
		    
	for k in range(0,23):
		if sequence2[i] != matrix[0][b]:
			b = b+1
		else:
			row = b+1
			#print(row)
			break
		    
	pamscore = pamscore + float(matrix[row][col])

print(pamscore)
'''

matrices_reader()
