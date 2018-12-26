import os
import sys
import itertools

f=open(os.path.join(sys.path[0], "input.txt"), "r")
f1=open(os.path.join(sys.path[0], "output.txt"), "w")

for line1,line2 in itertools.zip_longest(*[f]*2):
    char1,char2=[],[]
    if line1:
        for l in line1.rstrip("\n"):
            char1.append(l)
    if line2:
        for l in line2.rstrip("\n"):
            char2.append(l)
                  
    str1=''.join(map(str, itertools.chain.from_iterable((char1, char2))))
    f1.write(str1+"\n")
f.close()
f1.close()

'''
############################################################################
#INPUT file
############################################################################
17822715
fbaeecfd
12349999
fedc
42
the meaning of life
end
############################################################################
#OUTPUT File
############################################################################
17822715fbaeecfd
12349999fedc
42the meaning of life
end
'''
