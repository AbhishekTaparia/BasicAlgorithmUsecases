words=['qwertqw','asdvhjervasd','zaqwsnezaqw','asdvhjasdervasd','that','ashdfuah','asdfgasdfg','aaaa','abcababc']
#print(words)

def checkSuffixPrefix(word):
    # print(word[-2:-1]+word[len(word)-1])
    # if word[0]==word[len(word)-1]:
    #     return True;
    # if word[0:2]==word[-2:-1]+word[len(word)-1]:
    #     return True;
    # if word[0:3]==word[-3:-1]+word[len(word)-1]:
    #     return True;
    # print(word[:-2-1])
    ct=0
    for i in range(len(word)):
        j=i-i*2;  #j=-1*i
        if word[0:i]==word[j:]:
            ct=i
    return ct;
        


for i in words:
    print(checkSuffixPrefix(i)) 