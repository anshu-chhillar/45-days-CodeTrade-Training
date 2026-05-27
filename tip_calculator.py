#tip_calculator.py calculates tip amount and total bill 

#return sends value back from functions and result can be reused while print only displays the output on screeen and result cannot be reused

def calculate_tip(bill,tip_percent):
    tip = (bill * tip_percent) / 100
    total = bill + tip

    return{
        "tip" : tip,
        "total" : total
    }

bill1 = calculate_tip(1000, 10)
bill2 = calculate_tip(2500,15)
bill3 = calculate_tip(5000,20)

print("Bill 1:")
print(f"Tip Amount: {bill1['tip']}")
print(f"Total Amount: {bill1['total']}\n")

print("Bill 2:")
print(f"Tip Amount: {bill2['tip']}")
print(f"Total Amount: {bill2['total']}\n")

print("Bill 3:")
print(f"Tip Amount: {bill3['tip']}")
print(f"Total Amount: {bill3['total']}\n")