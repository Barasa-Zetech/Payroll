# Python program to calculate payroll;

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, basic_salary, allowance):
        super().__init__(id, name)
        self.basic_salary = basic_salary
        self.allowance = allowance

    def calculate_payroll_number(self):
        return self.basic_salary + self.allowance

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_pay):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_pay = hourly_pay

    def calculate_payroll_number(self):
        return self.hours_worked * self.hourly_pay

class CommissionEmployee(Employee):
    def __init__(self, id, name, basic_salary, allowance, commission):
        super().__init__(id, name)
        self.basic_salary = basic_salary
        self.allowance = allowance
        self.commission = commission

    def calculate_payroll_number(self):
        return self.basic_salary + self.allowance + self.commission

class PayrollCalculator:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll_number(self, employee):
        if isinstance(employee, SalaryEmployee):
            return f"ID: {employee.id}, Name: {employee.name}, Payroll: {employee.calculate_payroll_number()}"
        elif isinstance(employee, HourlyEmployee):
            return f"ID: {employee.id}, Name: {employee.name}, Payroll: {employee.calculate_payroll_number()}"
        elif isinstance(employee, CommissionEmployee):
            return f"ID: {employee.id}, Name: {employee.name}, Payroll: {employee.calculate_payroll_number()}"
        else:
            return f"ID: {employee.id}, Name: {employee.name}, Payroll: Unknown"


# Usage example
salary_employee = SalaryEmployee(1, "John Doe", 5000, 1000)
hourly_employee = HourlyEmployee(2, "Jane Smith", 160, 15)
commission_employee = CommissionEmployee(3, "Mike Johnson", 5000, 1000, 2000)

payroll_calculator1 = PayrollCalculator(1, "Payroll Calculator 1")
payroll_calculator2 = PayrollCalculator(2, "Payroll Calculator 2")
payroll_calculator3 = PayrollCalculator(3, "Payroll Calculator 3")

print(payroll_calculator1.calculate_payroll_number(salary_employee))
print(payroll_calculator2.calculate_payroll_number(hourly_employee))
print(payroll_calculator3.calculate_payroll_number(commission_employee))
