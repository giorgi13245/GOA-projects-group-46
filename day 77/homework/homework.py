def sum_digits(number):
    if number<0:
        number=str(number*-1)
    else:
        number=str(number)
        
    result=0
    for i in number:
        result+=int(i)
    return result

def change(st):
    new = ""
    st = st.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in st:
            new += "1"
        else:
            new += "0"
    return new

def sort_gift_code(code):
    return "".join(sorted(code))

def spin_words(sentence):
    list=sentence.split()
    result=[]
    for i in list:
        if len(i)>=5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)