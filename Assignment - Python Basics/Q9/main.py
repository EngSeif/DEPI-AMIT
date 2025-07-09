from funcs import calculator, checkFloatInput

operation_list = ["+", "-", "*", "/"] 

n1 = checkFloatInput("1st")
while n1 == None:
    n1 = checkFloatInput("1st")

n2 = checkFloatInput("2nd")
while n2 == None:
    n2 = checkFloatInput("2nd")

operation = input("choose one of the operations [\"+\", \"-\", \"*\", \"/\"] : ").strip()
while operation not in operation_list:
    print("Invalid Operation Choice")
    operation = input("choose one of the operations [\"+\", \"-\", \"*\", \"/\"] : ").strip()
    
print(f"Result : {calculator(n1, n2, operation)}")