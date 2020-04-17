principal = int(input("Enter amount: "))

rate = float(input("enter the percentage: "))

time = int(input("enter the period in years: "))

final_rate = float(rate/100)

simple_interest = principal * final_rate * time

print(simple_interest) 
