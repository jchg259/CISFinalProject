from matrices import PAMmatrices_reader
from galignment import nw_algoirthm
import numpy as np
import matplotlib.pyplot as plt

#Need to update so Lambda and K are inputs
def PAM_bitScore(PAMScore):
    L = 0.041
    K = 0.267
    PAMBitScore = (L*PAMScore - np.log(K))/np.log(2)
    return PAMBitScore

def PAM_Score_List(sequence_1, sequence_2):
    letters, matrixlist = PAMmatrices_reader()
    PAMlist = np.zeros(len(matrixlist))
    for i in range(len(matrixlist)):
        alignment_1, alignment_2, score = nw_algoirthm(sequence_1, sequence_2, letters, matrixlist[i])
        PAMlist[i] = score
    minPAM = np.min(PAMlist)
    maxPAMind = -1
    for i in range(50):
        if PAMlist[i] == minPAM:
            minPAMind = i
            break
    minPAMnum = (minPAMind+1)*10
    return minPAM, minPAMnum, PAMlist

def PAM_bitScoreList(PAMList):
    PAMBitScoreList = np.zeros(len(PAMList))
    for i in range(len(PAMList)):
        PAMBitScoreList[i] = PAM_bitScore(PAMList[i])

    return PAMBitScoreList
        
def PAM_Score_Graph(PAMlist):
    PAMMatrices = np.arange(10,510,10, dtype=int)
    plt.title("PAM Scores")
    plt.xlabel("PAM Matrices")
    plt.ylabel("PAM Scores")
    plt.plot(PAMMatrices, PAMlist, color ="red")
    plt.show()

def PAM_BitScore_Graph(PAMlist):
    PAMMatrices = np.arange(10,510,10, dtype=int)
    plt.title("Comparing PAMs")
    plt.xlabel("PAM Matrices")
    plt.ylabel("Scores (bits)")
    plt.plot(PAMMatrices, PAMlist, color ="red")
    plt.show()
