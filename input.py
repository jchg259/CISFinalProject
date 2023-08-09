from galignment import nw_algoirthm
from matrices import PAMmatrices_reader, BLOSUMmatrices_reader
from PAM import PAM_Score_List, PAM_Score_Graph
import numpy as np

#Ask if they want PAM or BLOSUM
#Offer to find global alignment for specific PAM/BLOSUM
#Offer to show alignment
#Create nicer UI
letters, PAMList = PAMmatrices_reader()
letters, BLOSUMList = BLOSUMmatrices_reader()

s1 = input("input sequence for protein one here:")
s2 = input("input sequence for protein two here:")

#make sure input is within letters given

#maxScore, BestPAM, PAMScorelist  = PAM_Score_List(s1, s2)
a1, a2, GA_Score = nw_algoirthm(s1,s2,letters,BLOSUMList[0])

#print("The maximum score is:", maxScore)
#print("This comes from PAM",BestPAM)
#print("The alignment is:","\n",a1,"\n",a2)
#print("Here is the full list of PAM Scores:", PAMScorelist)
#PAM_Score_Graph(PAMScorelist)

print(a1,"\n",a2)



