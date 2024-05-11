class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_salary(self, salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (salary / 50)
            total_salary = salary + overtime_amount
            return total_salary
        else:
            return salary

    def print_details(self):
        print("Employee Name:", self.emp_name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)


# Sample data
employee1 = Employee("Adams", "E7876", 50000, "Accounting")
employee2 = Employee("Jones", "E7499", 45000, "Research")
employee3 = Employee("Martin", "E7900", 50000, "Sales")
employee4 = Employee("Smith", "E7698", 55000, "Operations")

# Calculate and print details
employees = [employee1, employee2, employee3, employee4]
for employee in employees:
    print("\n")
    print("Employee Details:")
    employee.print_details()
    print("Total Salary:", employee.calculate_salary(employee.emp_salary, 55))
