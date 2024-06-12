"""
The LCM (Least Common Multiple) 
of two numbers is the smallest 
number that is a multiple of both 
numbers.


To find the LCM of 48 and 18, first, we need to find their prime factorization:

48 = 2 * 2 * 2 * 2 * 3 
18 = 2 * 3 * 3


Then, the LCM is the product of each prime factor raised to the highest power it occurs in either number:
    
    
LCM(48, 18) = (2^4) * (3^2) = 16 * 9 = 144


So, the LCM of 48 and 18 is 144.

"""

num1 = 48
num2 = 18
temp1 = num1
temp2 = num2


factorsLst1 = [ ]
factorsLst2 = [ ]


#-----------------------------------
"""
compare the following code with 
primefactors1.py and 
primefactors2.py
"""
for i in range (2, num1+1):
    while num1 % i == 0:
        print(f"num1 = {num1}")
        factorsLst1.append(i)
        num1 = num1// i # floor division = quotient
print(f"factorsLst1 = {factorsLst1}")
#-----------------------------------


for i in range (2, num2+1):
    while num2 % i == 0:
        print(f"num2 = {num2}")
        factorsLst2.append(i)
        num2 = num2// i  # floor division = quotient
print(f"factorsLst2 = {factorsLst2}")


dct1 = { }
for item in factorsLst1:
    dct1[item] = factorsLst1.count(item) # aaa_1
print(f"dct1 = {dct1}")


dct2 = { }
for item in factorsLst2:
    dct2[item] = factorsLst2.count(item)
print(f"dct2 = {dct2}")


#-----------------------------------
dct3 = { }


for key in dct1:
    try :
        maxValue = max(dct1[key], dct2[key]) # aaa_0
        dct3[key] = maxValue
    except KeyError: 
        dct3[key] = dct1[key]
        
        
for key in dct2:
    if key not in dct1:
        dct3[key] = dct2[key]
        
        
print(f"dct3 = {dct3}")
#-----------------------------------


lcm = 1
for key in dct3:
    lcm = lcm * pow(key, dct3[key])


num1 = temp1
num2 = temp2
print(f"LCM of {num1} and {num2} = {lcm}")
                

"""        
aaa_0
If a key exist in dct1 and if that key 
does not exist in dct2,  line aaa_0 
will raise a "KeyError".


Should a key in a dictionary be 
unique?


chatGPT : 

                
Yes, in Python, keys in a dictionary 
must be unique. If you try to assign 
a value to a key that already exists, 
it will overwrite the existing value.  
"""                                              
                