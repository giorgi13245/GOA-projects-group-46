#1
def lowercase_count(strng):
    result=0
    for i in strng:
        if i.islower():
            result+=1
    return result


#2
def capitals(word):
    result=[]
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result