word=[]
char=[]
n=len(word)
for i in word:
    count=0
    for j in char:
        if j in i:
            count+=1
    if count==len(char):
        print(i) 
    else:
       print('-1')
