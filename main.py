import RBTree
import re
sk= RBTree.RBTree()
file=open('EN-US-Dictionary.txt','r')
words = file.readlines()
rep=[]
file.close()
for word in words:
    rep.append(word.replace("\n",""))
for x in rep:
    sk.insert(x)
print('\nSize of the dictionary:' + str(sk.size1()))
print('\nHeight of the dictionary:' + str(sk.height1()))
#print(list(rep))
while(1):
    print('\nplease enter a word to search:')
    x=input()
    value=sk.search1(x)
    if value is None:
         print('NO! , not found')
    else:
        print('YES! , it is found')
    print('\nplease enter a word to insert:')
    y=input()
    found=sk.search1(y)
    if found is None:
        sk.insert(y)
        print("new number of word   " + str(sk.sizeoftree))
    else:
        print('ERROR : Word already in the dictionary!')


