#  Declare a dictionary with min 4 elements.
emp_details ={
#         1 : ("Suresh", 25, 25000, 2, 'Manager'), 
#         2 : ("Ramesh", 30, 30000, 7, 'Marketing Head'),
        1 : ("Suresh", 25, 25000, 2,), 
        2 : ("Ramesh", 30, 30000, 7,),
        3 : ("Mahesh", 25, 45000, 4),
        4 : ("Jayesh", 35, 100000, 10)
}
print(emp_details)

# Write a user defined function to add a new element in the dictionary

last_empid = max(emp_details.keys())
print(last_empid)

def inputempdetails():
    last_empid = max(emp_details.keys())
    last_empid+=1
    emp_name = input("Enter Eployee Name: ")
    emp_age  = int(input("Enter Employee Age"))
    emp_salary = int(input("Enter Employee Salary: "))
    emp_experience = int(input("Enter Employee Experience:"))
    emp_details[last_empid] = (emp_name, emp_age, emp_salary, emp_experience)

inputempdetails()
print(emp_details)

# Update the salary in the current dictionary with some condition.
for emp_id, details in emp_details.items():
    emp_name, emp_age, emp_salary, emp_experience = details
    if emp_age > 30 and emp_experience >= 5:
        emp_salary = int(emp_salary * 1.20)  # 20% increment
    elif emp_age > 28 and emp_experience >= 3:
        emp_salary = int(emp_salary * 1.15)  # 15% increment
    elif emp_age > 25 and emp_experience >= 2:
        emp_salary = int(emp_salary * 1.10)  # 10% increment
    else:
        emp_salary = int(emp_salary * 1.05)  # 5% increment
    emp_details[emp_id] = (emp_name, emp_age, emp_salary, emp_experience)
print(emp_details)


if len(emp_details) >= 2:
    second_last_key = list(emp_details.keys())[-2]
    removed_employee = emp_details.pop(second_last_key)
    print(f"Removed Employee ID: {second_last_key}")
print(emp_details)

import csv

csv_file = 'employee_details.csv'

# Write the dictionary to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['Employee ID', 'Name', 'Age', 'Salary', 'Experience', 'Designation'])
    
    # Write the data from the dictionary
    for emp_id, details in emp_details.items():
        writer.writerow([emp_id, *details])
