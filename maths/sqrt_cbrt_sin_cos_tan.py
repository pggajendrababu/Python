import math
X1 = 30 # degrees 
X2 = math.radians(X1)

Y1 = math.sqrt(X1)
Y2 = X1 ** (1/3) # pow(X1,(1/3))
Y3 = math.sin(X2)
Y4 = math.sinh(X2)


Y5 = math.cos(X2)
Y6 = math.cosh(X2)
Y7 = math.tan(X2)
Y8 = math.tanh(X2)


print("sqrt of ", X1, " = ", Y1)
print("cbrt of ", X1, " = ", Y2)
print("sin of ", X1, " = ", Y3)
print("sinh of ", X1, " = ", Y4)

print("-"*50)
print(f"cos of {X1} = {Y5}")
print(f"cosh of {X1} = {Y6}")
print(f"tan of {X1} = {Y7}")
print(f"tanh of {X1} = {Y8}")
print("-"*50)