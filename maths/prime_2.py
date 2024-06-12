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
        if number % i == 0: # mod function
            return False
    return True

user_input = int(input("Enter a number : "))
print("The following numbers are prime numbers")
print("-"*50)


for i in range(2, (user_input+1), 1):
   if is_prime(i):
       print(i)
   else:
       {} #pass

              
# another example : see aae_0_pass.py