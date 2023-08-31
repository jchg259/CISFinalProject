from input import SequenceInput, ScoringMatrixChoice, GlobalAlignment, OtherMatrix, SecondGlobalAlignment

s1, s2 = SequenceInput()
Best, Num = ScoringMatrixChoice(s1, s2)
GlobalAlignment(s1, s2, Best, Num)
Best_Two, Num_Two = OtherMatrix(s1, s2, Num)
SecondGlobalAlignment(s1, s2, Best_Two, Num_Two)
