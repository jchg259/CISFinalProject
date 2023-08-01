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
			matrixtext = matrixtext.replace("    ", " ")
			matrixtext = matrixtext.replace("     ", " ")
			matrixarray = np.fromstring(matrixtext, sep = ' ')
			matrixarray = matrixarray.reshape(24,24)
			matrixlist.append(matrixarray)
	
	return letters, matrixlist
            
	