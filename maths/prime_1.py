"""
There can be more than one return 
statements in a function. However, 
once the function executes a return 
statement, the function will exit. If 
your function does not need to 
return any value, you can omit the 
return statement. Alternatively, you 
can write return or return None .
"""

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main( ):
    user_input = int(input("Enter a number : "))
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
    
    
if __name__ == "__main__":
    main( )    
    