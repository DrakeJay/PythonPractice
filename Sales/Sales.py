weeks = int()
sales = float()
total = float()
avg_sales = float
weeks = int(input("Enter the number of weeks?  "))

for x in range(weeks):
  sales = float(input("Please enter the total dollar amount in sales:  "))
  total = total + sales
avg_sales = total / weeks
print("Total amount = " + str(total))
print("Average amount = " + str(avg_sales))