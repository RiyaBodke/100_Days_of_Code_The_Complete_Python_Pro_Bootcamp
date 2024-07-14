print("Welcome to tip calculator")

# Taking input of total bill
Total_bill = float(input(print("What was the total bill ? $ ")))

# Taking input of tip to be given 
tip = float(input(print("what percentage tip would you like to give ? 10, 12, or 15 ? ")))
total_tip = (Total_bill * tip)/100

# Taking input of the total number of people paying the bill and calculating total bill
no_of_people = int(input(print("How many people to split the bill ? "))) 
total = Total_bill + total_tip 

# Calculating individual amount to be paid
individual = round(total / no_of_people, 2)
print(f"Each person should pay : ${individual}")
