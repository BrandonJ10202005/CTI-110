#Brandon Johnson
#10/3/20233
#Use Float and Expressions to Calculate Gas Cost

#Create Input Variables
mpg = float(input("Enter the Car's Miles Per Gallon: "))
cpg = float(input("How much does a Gallon of Gasoline Cost?: "))

#Calculate Gas Cost Based on Gallons needed and Price per Gallon
#Calculate for: 20, 75, and 500 miles

cost_20 = (20/mpg) * cpg
cost_75 = (75/mpg) * cpg
cost_500 = (500/mpg) * cpg

#Output Values using the F string & format the floats
print(f"{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}")
