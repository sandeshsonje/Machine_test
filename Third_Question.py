'''3. Write a code that accepts the 2 lists and generates the following
result.
Employee = [‘Amit’,’Manish’,’Mahi’,’Kirti’,’Mafin’]
Salary = [20000,30000,20000,40000,25000]

Expected result of code:
{‘Amit’:20000,’Manish’:30000,’Mahi’:20000,’Kirti’:40000,’Mafin’:25000 }
'''
employee = []
n = int(input("Enter length of string = "))
for i in range(n):
    a = input("Enter string = ")
    employee.append(a)
print("Employee = ",employee)

salary = []
n1 = int(input("Enter length of number = "))
for i in range(n1):
    b = int(input("Enter number = "))
    salary.append(b)
print("Salary = ",salary)

myDict = {}
for i in range (len(employee)):
    myDict[employee[i]] = salary[i]
print(myDict)
