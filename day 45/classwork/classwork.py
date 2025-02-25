#1
def format_money(amount):
    
    return f"${amount:.2f}"



#2
def swap_values(args): 
    args[0], args[1]=args[1], args[0]


#3
def same_case(a, b): 
    if not a.isalpha() or not b.isalpha():
        return -1
    elif a.isupper() and b.isupper() or a.islower() or b.islower():
        return 1
    return 0


#4
def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
    


#5



#6
def calculate_age(year_of_birth, current_year):
    if year_of_birth - current_year==1:
        return f"You will be born in 1 year."
    elif current_year - year_of_birth==1:
        return f"You are 1 year old."
    elif year_of_birth==current_year:
        return f"You were born this very year!"
    elif year_of_birth<current_year:
        return f"You are {current_year-year_of_birth} years old."
    elif year_of_birth>current_year:
        return f"You will be born in {year_of_birth-current_year} years."