annual_interest_rate = 0.05
year = 12

monthly_income = int(input("Enter your monthly income: " ))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings =  monthly_income - monthly_expenses

projected_savings = monthly_savings * year +(monthly_savings * year * annual_interest_rate)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.0f}.")
