import math


def sin(deg):
    rad = math.radians(deg)
    x = math.sin(rad)
    y = round(x,4)
    return y
    
def main():
    deg = float(input("enter degrees : "))
    result = sin(deg)
    print(f"sin({deg}) = {result}")
    

if __name__ == "__main__":
    main()
