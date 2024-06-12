import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = 48
num2 = 18
print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))



# Example usage:
num1 = 48
num2 = 18
print("The GCD of", num1, "and", num2, "is", math.gcd(num1, num2))


"""
def gcd(a, b): - This line defines a 
function named gcd that takes two 
parameters, a and b, which 
represent the two numbers for 
which we want to find the greatest 
common divisor (GCD).    


while b: - This starts a while loop 
that continues as long as the value 
of b is non-zero. Since Python 
treats zero as False in a boolean 
context, this loop will terminate 
when b becomes zero.       


a, b = b, a % b - Inside the loop, the 
values of a and b are updated using 
tuple unpacking. a is assigned the 
current value of b, and b is 
assigned the remainder of a 
divided by b using the modulus 
operator %. This is the key step in 
the Euclidean algorithm for finding 
the GCD.    


return a - Once the while loop 
terminates (when b becomes zero), 
the function returns the value of a, 
which will be the GCD of the two 
numbers.
"""