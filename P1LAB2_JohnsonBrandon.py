#Brandon Johnson
#9/26/2023
#Calculates Travel Expenses

budget = int(input("Enter Budget: "))

dest = input("Where are you traveling? ")

gas = int(input("Enter Gas Budget: "))
food = int(input("Enter Food Budget: "))
hotel = int(input("Enter Hotel Budget: "))

expenses = gas+food+hotel

print("------Travel Expenses------")
print("Location: ", dest)
print("Initial Budget: ", budget)
print()
print("Gas Cost: ", gas)
print("Food Cost: ", food)
print("Hotel Cost: ", hotel)

print("Remaining Balance: ", budget-expenses)
