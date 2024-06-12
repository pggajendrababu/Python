num1 = 48
num2 = 18
divisorsLst1 = [ ]
divisorsLst2 = [ ]
commonDivisorsLst = [ ]


for i in range(1, num1+1):
    if num1 % i == 0:
        divisorsLst1.append(i)
#print(divisorsLst1)


for i in range(1, num2+1):
    if num2 % i == 0:
        divisorsLst2.append(i)
#print(divisorsLst2)


for item in divisorsLst1:
    if item in divisorsLst2:
        commonDivisorsLst.append(item)
#print(commonDivisorsLst)    

   
gcd =  max(commonDivisorsLst)
print(f"GCD of {num1} and {num2} = {gcd}")
        


