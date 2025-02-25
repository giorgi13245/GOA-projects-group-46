#1
def array(string):
    return " ".join(string.split(",")[1:-1]) or None
                        

#2
def temple_strings(obj, feature): 
    return f"{obj} are {feature}"


#3
def contamination(text, char):
  return char*len(text)

#4
def is_palindrome(s):
    s=s.lower()
    if s==s[::-1]:
        return True
    else:
        return False
    

#5
def obfuscate(email):
    return email.replace("@", " [at] ").replace(".", " [dot] ")