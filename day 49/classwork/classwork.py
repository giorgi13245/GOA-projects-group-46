#1
def replace_exclamation(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for a in s:
        if a in vowels:
            s = s.replace(a,'!')
    print(s)
    return s


#2
def get_size(w,h,d):
    area = 2*(w*h + h*d + w*d)
    volume = w*h*d
    return [area, volume]


#3



#4
def sp_eng(sentence): 
     return 'english' in sentence.lower()



#5
