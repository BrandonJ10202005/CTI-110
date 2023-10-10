#Brandon Johnson
#CTI-110
#10/10/2023
#P2HW2 - Working with lists

#Create Variables and get user input.
mod1 = float(input("Enter Module 1 Grade: "))
mod2 = float(input("Enter Module 2 Grade: "))
mod3 = float(input("Enter Module 3 Grade: "))
mod4 = float(input("Enter Module 4 Grade: "))
mod5 = float(input("Enter Module 5 Grade: "))
mod6 = float(input("Enter Module 6 Grade: "))

#Create an empty list.
gradelist = []

#Add variables to the list.
gradelist.append(mod1)
gradelist.append(mod2)
gradelist.append(mod3)
gradelist.append(mod4)
gradelist.append(mod5)
gradelist.append(mod6)

#Calculate Min, Max, Sum, and Average. Assign these to variables as well.
grademax = max(gradelist)
grademin = min(gradelist)
gradesum = sum(gradelist)
gradeavg = gradesum / len(gradelist)

#Display info to users with print statements.
print("\n----------Results------------")
print("Lowest Grade:", grademin)
print("Highest Grade:", grademax)
print("Sum of Grades:", gradesum)
print("Grade Average:", (f'{gradeavg:.2f}'))
print("-----------------------------")
