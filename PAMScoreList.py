from matrices import matrices_reader
from galignment import nw_algoirthm
import numpy as np

def PAM_Score_List(sequence_1, sequence_2):
    letters, matrixlist = matrices_reader()
    PAMlist = np.zeros(len(matrixlist))
    for i in range(len(matrixlist)):
        alignment_1, alignment_2, score = nw_algoirthm(sequence_1, sequence_2, letters, matrixlist[i])
        PAMlist[i] = score
    maxPAM = np.max(PAMlist)

    return maxPAM, PAMlist
        

