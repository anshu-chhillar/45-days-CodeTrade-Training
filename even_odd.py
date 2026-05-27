#even_odd.py checks whether a number is even, odd or zero

try:
    
    number = int(input("Enter a number: "))
    if number == 0:
        print("Number is zero.")
    elif number % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")

except ValueError:
    print("Invalid input! Please enter a valid number.")