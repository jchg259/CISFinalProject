from galignment import nw_algoirthm
from matrices import PAM_Score_List, matrices_reader
import numpy as np
import os


s1 = input("input sequence for protein one here:")
s2 = input("input sequence for protein two here:")

a1, a2 = nw_algoirthm(s1,s2)

PAMList = matrices_reader()

ScoreList = PAM_Score_List(a1, a2, PAMList)

BestPAM = max(ScoreList)

