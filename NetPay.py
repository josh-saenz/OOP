import EmployeeClass as e
import PayrollDeductionClass as p

employee = e.employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

deduction1 = p.PayrollDeduction('food court','8/14/2022', 22.50, 39119)
deduction2 = p.PayrollDeduction('gift contribution','8/12/2022', 25.00, 58475)
deduction3 = p.PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
deduction4 = p.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
deduction5 = p.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

#Report
print('*** Employee Pay ***')
print('Name:', employee.getName())
print('ID Number:', employee.getID())
print('Department:', employee.getDepartment())
print('Gross Pay: $', f'{employee.getSalary(): ,.2f}', sep = '')
print('Net Pay: $', f'{employee.getSalary()-deduction2.getCharge()-deduction4.getCharge()-deduction5.getCharge(): ,.2f}', sep = '')
