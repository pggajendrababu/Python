"""
-----------------------------
example : 7
1, 7 can divide 7
-----------------------------
If 2, 3, 4, 5, 6 does not divide 7,
then it is a prime number.
-----------------------------
so, if we check from 2 to 6,
that is enough.

so for loop should be like
for i in range(2, 6, 1):
-----------------------------    
"""


def isPrime(number):
    for i in range(2, number, 1):
        #print(f"i = {i}")
        #print(f"number = {number}")
        if number % i == 0:
            #print(f"{i} will divide {number}")
            return False
        #print("-"*10)
    return True


    
def main( ):
    
    
    number = int(input("Enter any integer value : "))
    
    
    lst = [ ]
    for i in range (2, number+1, 1):
        result = isPrime(i)
        if result == True:
            lst.append(i)
            
            
    print("\nFollowing numbers are")
    print("PRIME numbers")
    print("-"*40)
    for item in lst:
        print(item)  
   
        
                      
if __name__ == "__main__":
    main( )            