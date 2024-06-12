"""
1 USD = 83.002057 INR (03-01-2024)
=> 1 INR = (1/83.002057) USD
=> 15 INR = (15) * (1/83.002057)  USD
=> X INR = (X) * (1/83.002057) USD

1 Trillion = 1000,000,000,000 (1 followed by 12 zeros)

1 Billion = 1000,000,000 (1 followed by 9 zeros)

1 Million = 1000,000 (1 followed by 6 zeros)

100 thousands = 100,000 (1 followed by 5 zeros)

"""
USD = 83.002057
amount_to_be_multiplied = (1/USD)


def convert(amount_in_rupees):
    amount_in_dollars = amount_in_rupees * amount_to_be_multiplied
    return amount_in_dollars
     
                                            
def convert_block():
    #amount_in_rupees = 83002057000000
    amount_in_rupees = float(input("Enter amount in indian rupees : "))
    amount_in_dollars = convert(amount_in_rupees)
    if amount_in_dollars >= pow(10, 12):
        trillions = amount_in_dollars / pow(10, 12)
        print(f"{amount_in_rupees} INR = {trillions : ,} trillions USD")  
    elif amount_in_dollars >= pow(10, 9):
        billions = amount_in_dollars / pow(10, 9)
        print(f"{amount_in_rupees} INR = {billions : ,} billions USD")
    elif amount_in_dollars >= pow(10,6):
        millions = amount_in_dollars / pow(10, 6)
        print(f"{amount_in_rupees} INR = {millions : ,} millions USD")
    else:
        print(f"{amount_in_rupees} INR = {amount_in_dollars : ,} USD")    
        
    
def main():
    convert_block()                                                                
    

if __name__ == "__main__":
    main()            



