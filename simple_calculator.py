
def CALCULATOR(N1,N2,O):
    if N1.isdigit() and N2.isdigit():
        N1 = int(N1)
        N2 = int(N2)
    else:
        return -1
    if O == '+':
        return N1+N2
    elif O == '-':
        return N1-N2
    elif O == '*':
        return N1*N2
    elif O == '/':
        return N1/N2
    else:
        return -1


num1 = input("Enter the First Number: ")
num2 = input("Enter the Second Number: ")
operator = input("Enter the which operator has to perform: ")

Result = CALCULATOR(num1,num2,operator)

if Result == -1:
    print("Enter Valid Operant or Operator")
else:
    print(f"Computation of {num1} and {num2} {operator} is {Result}")