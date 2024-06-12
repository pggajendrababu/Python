"""
1 USD = 83.002057 INR (03-01-2024)
=> X USD = (X) * (83.002057) INR

1 Trillion = 1000,000,000,000 (1 followed by 12 zeros)

1 Billion = 1000,000,000 (1 followed by 9 zeros)

1 Million = 1000,000 (1 followed by 6 zeros)

100 thousands = 100,000 (1 followed by 5 zeros)

"""
USD = 83.002057
amount_to_be_multiplied = USD


def convert_trillions(amount_in_trillions):
    amount_in_dollars =  amount_in_trillions  * pow(10, 12)
    result = amount_in_dollars * amount_to_be_multiplied
    return result
    
    
def convert_billions(amount_in_billions):
    amount_in_dollars =  amount_in_billions  * pow(10, 9)
    result = amount_in_dollars * amount_to_be_multiplied
    return result
    
        
def convert_millions(amount_in_millions):
    amount_in_dollars =  amount_in_millions  * pow(10, 6)
    result = amount_in_dollars * amount_to_be_multiplied
    return result
    
                       
def convert(amount_in_dollars):
    result = amount_in_dollars * amount_to_be_multiplied
    return result                                                              
   
   
def convert_trillions_block():
    #amount_in_trillions = 1
    amount_in_trillions = float(input("Enter amount in trillions (dollars) : "))
    indian_rupees = convert_trillions(amount_in_trillions)
    if indian_rupees >= pow(10, 7):
        crores = indian_rupees/pow(10, 7)
        print(f"{amount_in_trillions} trillions USD = {crores} crores INR")
    else:
        print(f"{amount_in_trillions} trillions USD = {indian_rupees} INR")
        
    
    
def convert_billions_block():
    #amount_in_billions = 1
    amount_in_billions = float(input("Enter amount in billions (dollars) : "))
    indian_rupees = convert_billions(amount_in_billions)
    if indian_rupees >= pow(10, 7):
        crores = indian_rupees/pow(10, 7)
        print(f"{amount_in_billions} billions USD = {crores} crores INR")
    else:
        print(f"{amount_in_billions} billions USD = {indian_rupees} INR")
    
        
def convert_millions_block():
    #amount_in_millions = 1
    amount_in_millions = float(input("Enter amount in millions (dollars) : "))
    indian_rupees = convert_millions(amount_in_millions)
    if indian_rupees >= pow(10, 7):
        crores = indian_rupees/pow(10, 7)
        print(f"{amount_in_millions} millions USD = {crores} crores INR")
    else:
        print(f"{amount_in_millions} millions USD = {indian_rupees} INR")
    
                   
def convert_block():
    #amount_in_dollars = 1
    amount_in_dollars = float(input("Enter amount in dollars : "))
    indian_rupees = convert(amount_in_dollars)
    if indian_rupees >= pow(10, 7):
        crores = indian_rupees/pow(10, 7)
        print(f"{amount_in_dollars} USD = {crores} crores INR")
    else:
        print(f"{amount_in_dollars} USD = {indian_rupees} INR")                                                               
    
    
def main():
    #convert_trillions_block()
    #convert_billions_block()
    #convert_millions_block()
    convert_block()
    
if __name__ == "__main__":
    main()            



