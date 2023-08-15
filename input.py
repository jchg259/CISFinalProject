from galignment import nw_algoirthm
from matrices import PAMmatrices_reader, BLOSUMmatrices_reader
from PAM import PAM_Score_List, PAM_Score_Graph
from BLOSUM import BLOSUM_Score_List, BLOSUM_Score_Graph
import numpy as np


#Have user enter sequences
def SequenceInput():
    sequence1 = input("Please enter your first sequence here:").upper()
    sequence2 = input("Please enter your second sequence here:").upper()
    return sequence1, sequence2

#Decide which matrices you want to look at - Get matrices list, graph, best scoring matrix
def ScoringMatrixChoice(sequence1, sequence2):
    ScoringType = input("Enter PAM if you would like to compare PAM Matrices. Enter BLOSUM if you would like to compare BLOSUM Matrices.")
    if ScoringType.upper() not in ["PAM", "BLOSUM"]:
        print("That is not one of the options.")
        return ScoringMatrixChoice(sequence1, sequence2)
    elif ScoringType == "PAM":
        letters, PAMList = PAMmatrices_reader()
        minPAMScore, BestPAM, PAMScoreList = PAM_Score_List(sequence1, sequence2)
        print("Here is a list of the Scores:", PAMScoreList)
        PAM_Score_Graph(PAMScoreList)
        print("The best score is: ", minPAMScore, "and comes from the scoring matrix PAM",BestPAM)
        return BestPAM, 1
    else:
        letters, BLOSUMList = BLOSUMmatrices_reader()
        maxBLOSUMScore, BestBLOSUM, BLOSUMScoreList = BLOSUM_Score_List(sequence1, sequence2)
        print("Here is a list of the Scores:", BLOSUMScoreList)
        BLOSUM_Score_Graph(BLOSUMScoreList)
        print("The best score is: ", maxBLOSUMScore, "and comes from the scoring matrix BLOSUM",BestBLOSUM)
        return BestBLOSUM, 2

#Would you like to see the alignment with the best scoring matrix
def GlobalAlignment(sequence1, sequence2, Best, num):
    answer = input("Would you like to see the global alignment for the best scoring matrix? (yes/no)")
    if answer.lower() not in ["yes", "no"]:
        print("That is not one of the options. Please answer yes or no")
        return GlobalAlignment(sequence1, sequence2, Best, num)
    elif answer.lower() == "yes":
        if num == 1:
            letters, PAMList = PAMmatrices_reader()
            index = int((Best/10)-1)
            a1, a2, score = nw_algoirthm(sequence1, sequence2, letters, PAMList[index])
            print(a1, "\n", a2, sep="")
            return
        if num == 2:
            letters, BLOSUMList = BLOSUMmatrices_reader()
            BLOSUMMatrices = np.array([30, 35, 40, 45, 50, 55, 60, 62, 65, 70, 75, 80, 85, 90, 100])
            index = np.where(BLOSUMMatrices==Best)[0][0]
            a1, a2, score = nw_algoirthm(sequence1, sequence2, letters, BLOSUMList[index])
            print(a1, "\n", a2, sep="")
            return
    else:
        return

#Would you like to see the other scoring matrices
def OtherMatrix(sequence1, sequence2, num):
    answer = input("Would you like to see the scores from the other scoring matrices? (yes/no)")
    if answer.lower() not in ["yes", "no"]:
        print("That is not one of the options. Please answer yes or no")
        return OtherMatrix(sequence1, sequence2, num)
    elif answer.lower() == "yes":
        if num == 1:
            letters, BLOSUMList = BLOSUMmatrices_reader()
            maxBLOSUMScore, BestBLOSUM, BLOSUMScoreList = BLOSUM_Score_List(sequence1, sequence2)
            print("Here is a list of the Scores:", BLOSUMScoreList)
            BLOSUM_Score_Graph(BLOSUMScoreList)
            print("The best score is: ", maxBLOSUMScore, "and comes from the scoring matrix BLOSUM",BestBLOSUM)
            return BestBLOSUM, 3
        if num == 2:
            letters, PAMList = PAMmatrices_reader()
            minPAMScore, BestPAM, PAMScoreList = PAM_Score_List(sequence1, sequence2)
            print("Here is a list of the Scores:", PAMScoreList)
            PAM_Score_Graph(PAMScoreList)
            print("The best score is: ", minPAMScore, "and comes from the scoring matrix PAM",BestPAM)
            return BestPAM, 4
    else:
        print("Great! Thanks for using this program.")
        return 0, 5

def SecondGlobalAlignment(sequence1, sequence2, Best, num):
    if num == 5:
        exit
    else:
        answer = input("Would you like to see the global alignment for the best scoring matrix? (yes/no)")
        if answer.lower() not in [ "yes", "no"]:
            print("That is not one of the options. Please answer yes or no")
            return GlobalAlignment(sequence1, sequence2, Best, num)
        elif answer.lower() == "yes":
            if num == 4:
                letters, PAMList = PAMmatrices_reader()
                index = int((Best/10)-1)
                a1, a2, score = nw_algoirthm(sequence1, sequence2, letters, PAMList[index])
                print(a1, "\n", a2, sep="")
                return
            if num == 3:
                letters, BLOSUMList = BLOSUMmatrices_reader()
                def ind(array, item):
                    for idx, val in np.ndenumerate(array):
                        if val == item:
                            return idx
                index = int(ind(BLOSUMList, Best))
                a1, a2, score = nw_algoirthm(sequence1, sequence2, letters, BLOSUMList[index])
                print(a1, "\n", a2, sep="")
                return
        else:
            print("Great! Thanks for using this program.")
            return


