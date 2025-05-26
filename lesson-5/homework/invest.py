def invest(amount, rate, years):
    new_amount = amount * (rate + 1)
    for i in range(years):
        print(f"year {i+1}: ${new_amount}")
        new_amount = round((new_amount * (rate + 1)), 2)

amount = input("Enter an initial amount: ")
rate = input("Enter a rate: ")
years = input("Enter years: ")

try:
    amount = float(amount)
    rate = float(rate)
    years = int(years)
    invest(amount, rate, years)
except:
    print("Please enter only numbers")