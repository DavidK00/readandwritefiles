import csv
from msilib.schema import IniFile

infile = open('EmployeePay.csv')
employee_pay = csv.reader(infile, delimiter = ',')

next(infile)

for record in employee_pay:
    print('First Name:', record[1])
    print('Last Name:', record[2])
    salary = float(record[3])
    print('Salary:', "${:,.2f}".format(salary))
    bonus = float(record[4]) * float(record[3])
    print('Bonus:', "${:,.2f}".format(bonus))
    total_pay = float(salary)+ (bonus)
    print('Total Pay:', "${:,.2f}".format(total_pay))
    input()
    