print("operations: ")
print("+. add")
print("-. subtract")
print("*. multiply")
print("/. divide")

choice = input("enter choice (+,-,*,/): ")

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if choice =='+':
    print(num1+num2)
if choice =='-':
    print(num1-num2)
if choice =='*':
    print(num1*num2)
if choice =='/':
    print(num1/num2)
if choice != '+' & choice != '-' & choice !='*' & choice != '/':
    print("Invalid Operator")
      