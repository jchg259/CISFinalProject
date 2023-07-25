from matrices import matrices_reader
from galignment import nw_algoirthm
import numpy as np
import matplotlib.pyplot as plt

def PAM_Score_List(sequence_1, sequence_2):
    letters, matrixlist = matrices_reader()
    PAMlist = np.zeros(len(matrixlist))
    for i in range(len(matrixlist)):
        alignment_1, alignment_2, score = nw_algoirthm(sequence_1, sequence_2, letters, matrixlist[i])
        PAMlist[i] = score
    maxPAM = np.max(PAMlist)
    maxPAMind = -1
    for i in range(25):
        if PAMlist[i] == maxPAM:
            maxPAMind = i
            break
    maxPAMnum = (maxPAMind+1)*10
    return maxPAM, maxPAMnum, PAMlist
        
def PAM_Score_Graph(PAMlist):
    PAMMatrices = np.arange(10,260,10, dtype=int)
    plt.title("PAM Scores")
    plt.xlabel("PAM Matrices")
    plt.ylabel("PAM Scores")
    plt.plot(PAMMatrices, PAMlist, color ="red")
    plt.show()