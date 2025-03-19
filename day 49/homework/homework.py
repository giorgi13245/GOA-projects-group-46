#1
def derive(coe, exp): 
    return f"{coe*exp}x^{exp-1}"


#2
def whatday(num):
    days = ["Wrong, please enter a number between 1 and 7", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if num < 1 or num > 7:
        return "Wrong, please enter a number between 1 and 7"
    else: return days[num]



#3
def create_array(n):
    res=[]
    for i in range(1,n+1):
        res.append(i)
    return res


#4
def is_leap_year(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
    

#5
def quote(fighter):
    if fighter.lower() == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return "I am not impressed by your performance."