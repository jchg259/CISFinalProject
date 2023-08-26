# CISFinalProject

This is a final project for my Master's in Computer Science through UMass Dartmouth. The purpose is to look at several scoring matrices and decide which gives the best global alignment. The user has the option to just see the best score for either PAM or BLOSUM scoring matrices. Beyond that the user can see the best global alignment, see the best score for the group of scoring matrices they did not choose and finally see that global alignment. 

matrices.py is used to read the matrices from the folders BLOSUMMatrices and PAMMatrices
PAM.py has the PAM specific programs and BLOSUM.py has the BLOSUM specific programs. Both have programs that can create a list of PAMScores and an appropriate graph. 
galignment.py uses the Needleman-Wunsch algorithm and mapping to find the global alignment given one scoring matrix
input.py has the programs that gets the user input and puts the various programs together so that the user interface can be cleaner. 
Main.ipynb is a Jupyter Notebook that is where the user interface lies. 

Sources of significant inspiration come from the following: 
https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/

https://github.com/UnaStankovic/ProteinNucleotideSequenceAlignment

https://drive.google.com/file/d/1lmuaSI3142z_MzctOlmR7NAQUelK0hCF/view
