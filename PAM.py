from matrices import PAMmatrices_reader
from galignment import nw_algoirthm
import numpy as np
import matplotlib.pyplot as plt



def PAM_Score_List(sequence_1, sequence_2):
    letters, matrixlist, Llist, Klist = PAMmatrices_reader()
    PAMlist = np.zeros(len(matrixlist))
    for i in range(len(matrixlist)):
        alignment_1, alignment_2, score = nw_algoirthm(sequence_1, sequence_2, letters, matrixlist[i])
        PAMlist[i] = score
    minPAM = np.min(PAMlist)
    minPAMind = -1
    for i in range(50):
        if PAMlist[i] == minPAM:
            minPAMind = i
            break
    minPAMnum = (minPAMind+1)*10

    return minPAM, minPAMnum, PAMlist

def PAM_Bit_Score_List(sequence_1, sequence_2):
    letters, matrixlist, Llist, Klist = PAMmatrices_reader()
    PAMBitlist = np.zeros(len(matrixlist))
    for i in range(len(matrixlist)):
        alignment_1, alignment_2, score = nw_algoirthm(sequence_1, sequence_2, letters, matrixlist[i])
        PAMBitlist[i] = (float(Llist[i])*score- np.log(float(Klist[i])).item())/(np.log(2).item())
    return PAMBitlist


def PAM_Score_Graph(PAMlist):
    PAMMatrices = np.arange(10,510,10, dtype=int)
    plt.title("Comparing PAMs")
    plt.xlabel("PAM Matrices")
    plt.ylabel("PAM Scores")
    plt.plot(PAMMatrices, PAMlist, color ="red")
    plt.show()

def PAM_BitScore_Graph(PAMBitlist):
    PAMMatrices = np.arange(10,510,10, dtype=int)
    plt.title("Comparing PAMs")
    plt.xlabel("PAM Matrices")
    plt.ylabel("Scores (bits)")
    plt.plot(PAMMatrices, PAMBitlist, color ="green")
    plt.show()
