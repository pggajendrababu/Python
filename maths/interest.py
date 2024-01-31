from datetime import datetime

def simple(P, interest_rate, months):
    # P = principal
    # r = annual interest rate (as a decimal)
    # t = time in years
    
    
    r = (interest_rate/100)
    t = months/12
    interest = P * r * t
    return interest
    
    
def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    
    date1 = datetime.strptime(date_str1, date_format)
    #print(date1)
    date2 = datetime.strptime(date_str2, date_format)
    
    delta = date2 - date1
    #print(delta)
    
    return abs(delta.days)
    

def compound(P, interest_rate, n, t):
    # compound interest
    # P = principal
    # r = annual nominal interest rate (as a decimal)
    # n = number of times the interest is compounded per year
    # t = number of years
    # A = accrued interest
    
    
    r = (interest_rate/100)
    base = 1+(r/n)
    power = n * t
    A = P * (base ** power)
    return A
    

def principal(A, interest_rate, n, t):
    # P = principal
    # r = annual nominal interest rate (as a decimal)
    # n = number of times the interest is compounded per year
    # t = number of years
    # A = accrued interest
    
    
    r = (interest_rate/100)
    base = 1+(r/n)
    power = n * t
    P = A/(base ** power)
    return P
    
    
def interest(A, P, n, t):
    # P = principal
    # r = annual nominal interest rate (as a decimal)
    # n = number of times the interest is compounded per year
    # t = number of years
    # A = accrued interest
    
    
    base = A/P
    power = 1/(n * t)
    interest = ((base ** power)-1) * n
    return interest
    

def simple_block():
    P = 100000
    interest_rate = 12
    months = 3
    
    simple_interest = simple(P, interest_rate, months)
    print(f"Principal : {P}")
    print(f"Interest rate : {interest_rate}")
    print(f"months : {months}")
    print(f"Simple interest : {simple_interest}")
    
    
def days_between_dates_block():
    # Example usage
    date1 = "2022-01-01"
    date2 = "2022-12-31"
    
    result = days_between_dates(date1, date2)
    print(f"Number of days between {date1} and {date2}: {result} days")
    
    
def compound_block():
    P = 100000
    interest_rate = 12
    n = 365
    from_date = "2024-01-24"
    to_date = "2044-01-24"
    t = (days_between_dates(from_date, to_date)/365)
    
    
    #P = float(input("Enter principal amount : "))
    #interest_rate = float(input("Enter interest rate : "))
    #n = int(input("Enter the number of times the interest should be compounded : "))
    #from_date = str(input("Enter 'from date' : "))
    #to_date = str(input("Enter 'to date' : "))
    #t = (days_between_dates(from_date, to_date)/365)
    
   
    compound_interest = compound(P, interest_rate, n, t)
    
    print(f"Principal : {P}")
    print(f"Interest rate : {interest_rate}")
    print(f"Number of times the interest is compounded : {n}")
    print(f"From date : {from_date}")
    print(f"To date : {to_date}")
    print(f"Compound interest : {compound_interest}")
    
       
def principal_block():
    A = 1100000
    interest_rate = 12
    n = 365
    from_date = "2024-01-24"
    to_date = "2044-01-24"
    t = (days_between_dates(from_date, to_date)/365)
    
    
    #A = float(input("Enter compound interest: "))
    #interest_rate = float(input("Enter interest rate : "))
    #n = int(input("Enter the number of times the interest should be compounded : "))
    #from_date = str(input("Enter 'from date' : "))
    #to_date = str(input("Enter 'to date' : "))
    #t = (days_between_dates(from_date, to_date)/365)
    
   
    principal_amount = principal(A, interest_rate, n, t)
    
    
    print(f"Compound interest: {A}")
    print(f"Interest rate : {interest_rate}")
    print(f"Number of times the interest is compounded : {n}")
    print(f"From date : {from_date}")
    print(f"To date : {to_date}")
    print(f"Principal required : {principal_amount}")
    
    
def interest_block():
    A = 1157011.8350217324
    P = 100000
    n = 365
    from_date = "2024-01-24"
    to_date = "2044-01-24"
    t = (days_between_dates(from_date, to_date)/365)
    
    
    #A = float(input("Enter compound interest: "))
    #interest_rate = float(input("Enter interest rate : "))
    #n = int(input("Enter the number of times the interest should be compounded : "))
    #from_date = str(input("Enter 'from date' : "))
    #to_date = str(input("Enter 'to date' : "))
    #t = (days_between_dates(from_date, to_date)/365)
    
   
    interest_rate = round((interest(A, P, n, t))*100,2)
    
    
    print(f"Compound interest: {A}")
    print(f"Principal : {P}")
    print(f"Number of times the interest is compounded : {n}")
    print(f"From date : {from_date}")
    print(f"To date : {to_date}")
    print(f"Interest rate : {interest_rate}")
    
        
def main():
    
    #simple_block()
    #days_between_dates_block()
    compound_block()
    #principal_block()
    #interest_block()
    
    
    

if __name__ == "__main__":
    main()
