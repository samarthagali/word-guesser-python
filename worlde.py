# Import the modules required
from nltk.corpus import words
import random
import re
word_list = words.words()


def  guess():
    b=random.choice(word_list)
    if len(b)<=7:
        return b
    else:
        return guess()
c=guess()
ng=5
fin=""

corr=[]
while(ng>=0):
    if len(corr)==len(c):
        print("congrats you won")
        
        break
    else:
        d="_ "*len(c)
        print(d)
        a=(input("enter a letter which you think is present in the above word (_) indicates not filled (please input one letter otherwise it's wrong):"))
        l=[]
        pos=""
        if a in c and len(a)==1:
            for i in range(len(c)) :
                if c[i]==a:
                    l.append(i)
                    
            corr.append(a)
            for i in l:
                pos+=str(i)
                pos+="&"
            print(a,"is in positions",pos)
        else:
            print("wrong , you have",ng,"guesses remaining")
            ng-=1
print("the word was",c)   