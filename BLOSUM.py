from matrices import BLOSUMmatrices_reader
from galignment import nw_algoirthm
import numpy as np
import matplotlib.pyplot as plt

#Need to update so Lambda and K are inputs
def PAM_bitScore(PAMScore):
    #L = 0.041
    #K = 0.267
    K = 0.279
    L = 0.058
    PAMBitScore = (L*PAMScore - np.log(K))/(np.log(2))
    return PAMBitScore

def BLOSUM_Score_List(sequence_1, sequence_2):
    letters, matrixlist = BLOSUMmatrices_reader()
    BLOSUMMatrices = np.array([30, 35, 40, 45, 50, 55, 60, 62, 65, 70, 75, 80, 85, 90, 100])
    BLOSUMlist = np.zeros(len(matrixlist))
    for i in range(len(matrixlist)):
        alignment_1, alignment_2, score = nw_algoirthm(sequence_1, sequence_2, letters, matrixlist[i])
        BLOSUMlist[i] = score
    maxBLOSUM = np.max(BLOSUMlist)
    maxPAMind = -1
    for i in range(50):
        if BLOSUMlist[i] == maxBLOSUM:
            maxBLOSUMind = i
            break
    maxBLOSUMnum = BLOSUMMatrices[maxBLOSUMind]
    return maxBLOSUM, maxBLOSUMnum, BLOSUMlist

def PAM_bitScoreList(PAMList):
    PAMBitScoreList = np.zeros(len(PAMList))
    for i in range(len(PAMList)):
        PAMBitScoreList[i] = PAM_bitScore(PAMList[i])

    return PAMBitScoreList
        
def BLOSUM_Score_Graph(BLOSUMlist):
    BLOSUMMatrices = np.array([30, 35, 40, 45, 50, 55, 60, 62, 65, 70, 75, 80, 85, 90, 100])
    plt.title("Comparing BLOSUMs")
    plt.xlabel("BLOSUM Matrices")
    plt.ylabel("BLOSUM Scores")
    plt.plot(BLOSUMMatrices, BLOSUMlist, color ="blue")
    plt.show()

def PAM_BitScore_Graph(PAMlist):
    PAMMatrices = np.arange(10,510,10, dtype=int)
    plt.title("Comparing PAMs")
    plt.xlabel("PAM Matrices")
    plt.ylabel("Scores (bits)")
    plt.plot(PAMMatrices, PAMlist, color ="red")
    plt.show()