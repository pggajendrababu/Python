def magic_box(num):
    num22 = num/5
    
    num21 = num22 - 1
    num20 = num21 - 1
    
    num14 = num20 - 1
    num13 = num14 - 1
    num12 = num13 - 1
    num11 = num12 - 1
    num10 = num11 - 1
    
    num04 = num10 - 1
    num03 = num04 - 1
    num02 = num03 - 1
    num01 = num02 - 1
    num00 = num01 - 1
    
    num23 = num22 + 1
    num24 = num23 + 1
    
    num30 = num24 + 1
    num31 = num30 + 1
    num32 = num31 + 1
    num33 = num32 + 1
    num34 = num33 + 1
    
    num40 = num34 + 1
    num41 = num40 + 1
    num42 = num41 + 1
    num43 = num42 + 1
    num44 = num43 + 1
    
    # shifting part
    
    target00 = num02
    target01 = num30
    target02 = num13
    target03 = num41
    target04 = num24
    
    target10 = num34
    target11 = num12
    target12 = num40
    target13 = num23
    target14 = num01
    
    target20 = num11
    target21 = num44
    target22 = num22
    target23 = num00
    target24 = num33
    
    target30 = num43
    target31 = num21
    target32 = num04
    target33 = num32
    target34 = num10
    
    target40 = num20
    target41 = num03
    target42 = num31
    target43 = num14
    target44 = num42
    
    # displaying part
    
    message = "If you add horizontally or vertically or diagonally, you will get "
    print(f"\n{message}{num}.\n")
    
    lst1 = [target00, target01, target02, target03, target04,
    target10, target11, target12, target13, target14,
    target20, target21, target22, target23, target24,
    target30, target31, target32, target33, target34,
    target40, target41, target42, target43, target44]
    
    lst2 = [ ]
    for item in lst1:
        lst2.append(str(int(item)).rjust(10))
        
    for i in range(0, len(lst2)-1, 5):
        print(lst2[i], lst2[i+1], lst2[i+2], lst2[i+3], lst2[i+4])
    
            
def magic_box_block():
        num = int(input("Enter any number which is divisible by 5 : "))
        #num = 100
        if num%5 == 0:
            magic_box(num)
        else:
            print("Entered number is not divisible by 5. Try again.")


def main():
    magic_box_block()


if __name__ == "__main__":
    main()