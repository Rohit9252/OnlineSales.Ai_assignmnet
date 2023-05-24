import csv

# Function to calculate average salary
def calculate_average_salary(salaries):
    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)
    return round(average_salary, 2)

# Read departments from departments.csv
departments = {}
with open('departments.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        department_id = int(row[0])
        department_name = row[1]
        departments[department_id] = department_name

# Read employees from employees.csv
employees = {}
with open('employees.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        employee_id = int(row[0])
        employee_name = row[1]
        department_id = int(row[2])
        employees[employee_id] = (employee_name, department_id)

# Read salaries from salaries.csv
salaries = {}
with open('salaries.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        employee_id = int(row[0])
        month = row[1]
        salary = int(row[2])
        if employee_id in salaries:
            salaries[employee_id].append(salary)
        else:
            salaries[employee_id] = [salary]

# Calculate average monthly salary for each department
department_salaries = {}
for employee_id, (employee_name, department_id) in employees.items():
    if department_id in departments:  # Check if department ID is valid
        if department_id in department_salaries:
            department_salaries[department_id].extend(salaries[employee_id])
        else:
            department_salaries[department_id] = salaries[employee_id]
    else:
        print(f"Invalid department ID for employee {employee_id}")

# Generate the report
print("DEPT_NAME ", " AVG_MONTHLY_SALARY (USD)")
print()

# Sort departments by average salary in descending order
sorted_departments = sorted(department_salaries.items(), key=lambda x: calculate_average_salary(x[1]), reverse=True)

# Display top 3 departments
for i in range(3):
    department_id, salaries = sorted_departments[i]
    department_name = departments.get(department_id, "Unknown")
    average_salary = calculate_average_salary(salaries)
    print(department_name," ", average_salary)
    print()
