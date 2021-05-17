from txtToHash import prehash
import time
from sys import argv

""" 
Input your source file and your prehashed file name respectively
on the command line.

*Tested on windows only
"""

dictFile = 'names.txt'
hashFile = 'hashed.txt'
if len(argv) > 1:
    dictFile = argv[1]
    hashFile = argv[2]

def attack(dictFile, hashFile):
    st = time.time()
    userHash = input("Enter Hash: ")
    print("Matching....")
    st = time.time()
    prehash(dictFile, hashFile)
    f = open(hashFile, 'r')
    index = 0
    prehashList = (f.read()).split('\n')
    for i in prehashList:
        index += 1
        if userHash == i:
            print(f"Found a match at index {index}")
            f.close()
            origin = open(dictFile, 'r')
            match = (origin.read()).split('\n')
            print(f"Phrase is {match[index-1]}")
            break
        elif index >= len(prehashList):
            print("Not found")
    print(f"Time Taken {time.time()-st} secs")
if __name__ == '__main__':
    if len(argv)==4:
            if argv[3] == 'p':
                print("Prehashing for optimaization....")
                prehash(dictFile, hashFile)
                print("Process complete")
    else:
        attack(dictFile, hashFile)