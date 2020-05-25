import itertools

def checkAnagram(text,word):
    lWord=len(word)
    lText=len(text)
    # ct=0
    anagramList=[]
    if len(word) <=1:
        return word;
    else:
        for i in checkAnagram(text,word):
            for j in range(len(word)):
                temp.append(i[:j]+word[0:1]+word[j:])
        return temp    


    # for i in word:
    #     for j in range(lWord):
    #         if i in text[j:j+lWord]

print(checkAnagram("datatada","tada"))