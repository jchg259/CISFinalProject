import numpy as np

sequence1 = "GAVLIMXCST"
sequence2 = "GAV-YZXC--"



matrix = np.loadtxt("Matrices/PAM10.txt", dtype=str)

n = len(sequence1)
m = len(sequence2)

pamscore = 0

for i in range(0,max(n,m)):
	a=0
	b=0
	for j in range(0,n):
		if sequence1[i] != matrix[0][a]:
			a = a+1
		else:
			col = a
			break
	for j in range(0,m):
		if sequence2[i] != matrix[0][a]:
			b = b+1
		else:
			row = b+1
			break
	pamscore = pamscore + float(matrix[row][col])

print(pamscore)
