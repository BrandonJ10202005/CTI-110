#Brandon Johnson
#10/19/2023
#Working with nested and unnested if else statements


#Create a boolean variable to hold leap year status
is_leap = False

#Get year from the user
year = int(input("Enter a year to determine if it's a leap year: "))

#Does year divide by 4
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

#print output to user
if is_leap == True:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is NOT a leap year")
