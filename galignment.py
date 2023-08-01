#Adapted from program by Bineet Kumar Mohanta

import numpy as np


def nw_algoirthm(sequence_1, sequence_2,letters, SCORE_matrix):

#Create Matrices
    main_matrix = np.zeros((len(sequence_1)+1,len(sequence_2)+1))
    match_checker_matrix = np.zeros((len(sequence_1),len(sequence_2)))
    

# Providing the scores for match ,mismatch and gap

    gap_penalty = SCORE_matrix[0][23]

    #print(match_checker_matrix)
    map = {"A":0, "R":1, "N":2, "D":3, "C":4, "Q":5, "E":6, "G":7, "H":8, "I":9, "L":10, "K":11, "M":12, "F":13, "P":14, "S":15, "T":16, "W":17, "Y":18, "V":19, "B":20, "Z":21, "X":22}
    def match_checker_score(a, b):
        
        return SCORE_matrix[map[a]][map[b]]


#Filling up the matrix using Needleman_Wunsch algorithm
#STEP 1 : Initialisation
    for i in range(len(sequence_1)+1):
        main_matrix[i][0] = i * gap_penalty
    for j in range(len(sequence_2)+1):
        main_matrix[0][j] = j * gap_penalty

#STEP 2 : Matrix Filling
    for i in range(1,len(sequence_1)+1):
        for j in range(1,len(sequence_2)+1):
            main_matrix[i][j] = max(main_matrix[i-1][j-1]+ match_checker_score(sequence_1[i-1], sequence_2[j-1]), 
                                main_matrix[i-1][j]+gap_penalty,
                                main_matrix[i][j-1]+ gap_penalty)

    #print(main_matrix)

# STEP 3 : Traceback

    aligned_1 = ""
    aligned_2 = ""

    ti = len(sequence_1)
    tj = len(sequence_2)

    GA_Score = 0

    while(ti >0 and tj > 0):

        GA_Score = GA_Score + main_matrix[ti][tj]
        if (ti >0 and tj > 0 and main_matrix[ti][tj] == main_matrix[ti-1][tj-1]+ match_checker_score(sequence_1[ti-1], sequence_2[tj-1])):#match_checker_matrix[ti-1][tj-1]):

            aligned_1 = sequence_1[ti-1] + aligned_1
            aligned_2 = sequence_2[tj-1] + aligned_2

            ti = ti - 1
            tj = tj - 1

    
        elif(ti > 0 and main_matrix[ti][tj] == main_matrix[ti-1][tj] + gap_penalty):
            aligned_1 = sequence_1[ti-1] + aligned_1
            aligned_2 = "-" + aligned_2

            ti = ti -1
        else:
            aligned_1 = "-" + aligned_1
            aligned_2 = sequence_2[tj-1] + aligned_2

            tj = tj - 1

#test
    #print(aligned_1)
    #print(aligned_2)
    #print(GA_Score)
    return aligned_1, aligned_2, GA_Score
