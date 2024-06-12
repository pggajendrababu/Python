import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Example usage:
num1 = 48
num2 = 18
print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))



# Example usage:
num1 = 48
num2 = 18
print("The LCM of", num1, "and", num2, "is", math.lcm(num1, num2))