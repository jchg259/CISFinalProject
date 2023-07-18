from galignment import nw_algoirthm
from matrices import PAM_Score
import numpy as np


s1 = input("input sequence for protein one here:")
s2 = input("input sequence for protein two here:")

a1, a2 = nw_algoirthm(s1,s2)

print(a1)
print(a2)
