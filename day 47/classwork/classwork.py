# 1


# 2
def dup(arry):
    result = []
    
    for i in arry:
        test = ""

        for x in range(len(i)):
            if test == "" or i[x] != test[-1]:
                test += i[x]
                
        result.append(test)
    return result



# 3
def spin_words(sentence):
    list=sentence.split()
    result=[]
    for i in list:
        if len(i)>=5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)


# 4





# 5
def min_value(digits):
    no_duplicates = []
    
    for i in digits:
        if i not in no_duplicates:
            no_duplicates.append(i)
    
    result = ""
    
    for i in sorted(no_duplicates):
        result += str(i)
    return int(result)


# 6
def max_multiple(divisor, bound):
    result=[]
    for i in range(0,bound+1):
        if i%divisor==0:
            result.append(i)
        else:
            continue
        
    return result[-1]



# 7
def alphabetic(s):
    return sorted(s)==list(s)


# 8
