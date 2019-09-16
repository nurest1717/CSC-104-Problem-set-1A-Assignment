# Taking users input 
annual_salary = float(input("What is your starting annual salary: "))
portion_saved = float(input("What portion of your salary is to be saved, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))




# Fixed Data 
portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12 
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment 
monthly_deposit = monthly_salary * portion_saved
 


# Initial savings(current_savings)
# The function is used to stop algorithm 
current_savings = 0.0


months = 0  #This would be helpful to hold the number of months after the algorithm


while current_savings < down_payment: 
    months += 1 #(this adds the initial value of months, add one and assign the resutl as new value of months)
    current_savings = current_savings * (1 + monthly_rate_of_return)
    current_savings += monthly_deposit # same as current_savings = current_savings + monthly_deposit 
    
    
print('Number of months', months)