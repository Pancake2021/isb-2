import math
from cmath import sqrt


sequence1 = [1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,]
#1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,9 0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1 33,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,0,1,1,0,1,1 53,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,]


s1 = sum(sequence1)
#59

tmp = s1/128
print (tmp)
#0.4609375

e1 = - (tmp - 0.5)
print (e1)
#0.0390625


e2 = (2/math.sqrt(128))
print (e2)
#0.17677669529663687

count = 0

# if (e1 < e2):
if (e1 < e2):
    for i in   range(len(sequence1)-1):
        sequence1[i] != sequence1[i+1] 
        count += 1
count += 1
    
print (count)
#66

P =  math.erfc((66-2*128*tmp*(1-tmp))/(2*math.sqrt(2*128)*tmp*(1-tmp)))
print(P)
#0.6706894158999841
#последовательность случайна