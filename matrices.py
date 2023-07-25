# Import Module
import os
import numpy as np
  
def matrices_reader():
	matrixlist = list()
	path = r"/Users/jgray/Documents/CIS Final Project/CISFinalProject/Matrices"
	
	# Change the directory
	os.chdir(path)
    
	def read_text_file(file_path):
		with open(file_path, 'r') as f:
			letters = str(f.readline())
			return letters, f.read()
  
	
    # iterate through all file
	for file in os.listdir():
        # Check whether file is in text format or not
		if file.endswith(".txt"):
			file_path = f"{path}/{file}"
	    
            # call read text file function and add each file to list
			#print(read_text_file(file_path))
			letters, matrixtext = read_text_file(file_path)
			matrixtext = matrixtext.replace("\n", "  ")
			matrixtext = matrixtext.replace("  ", " ")
			matrixtext = matrixtext.replace("   ", " ")
			matrixarray = np.fromstring(matrixtext, sep = ' ')
			matrixarray = matrixarray.reshape(24,24)
			matrixlist.append(matrixarray)
	
	return letters, matrixlist
            


#sequence1 and sequence2 are after global sequencing
#Computes PAM_Score (Note: consider putting inside PAMScoreList)
"""def PAM_Score(sequence1, sequence2, matrix):

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

	return pamscore
"""
#Create a list of all 50 PAM scores
	