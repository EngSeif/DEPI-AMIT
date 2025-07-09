# ================================ Helper Functions =========================================
def checkFloatInput(order):
    """
        checkFloatInput - check if entered Number is a Valid Float
        
        parameters : 
            - order (string) : Order of Number (Number one or Number two is entered)
             
        return :
            num  : if Number is a Valid Float
            None : if Number is a NOT Valid Float
    """
    try:
        num = float(input(f"Enter The {order} Number : "))
        return num
    except ValueError:
        print("Invalid Input Try Again")
        return None
        
                    
# ================================ Main Functions =========================================    

def calculator(num1, num2, operation):
    """
        calculator - evaluate the expression Given two numbers and the Operator
        
        parameters : 
            - num1 (float) : first Number of operation
            - num2 (float) : second number of operation
            - operation (float) : Operation to be done on the two numbers
             
        return :
            result  : number resulted from operation
            None    : if there is a division by zero
    """
    
    def sum(n1, n2):
        """
            sum - returns summation of n1 and n2 
        """
        return n1 + n2
    
    def subtract(n1, n2):
        """
            subtract - returns subtraction of n2 from n1
        """
        return n1 - n2
    
    def multiply(n1, n2):
        """
            multiply - returns multiplication of n1 and n2
        """
        return n1 * n2
    
    def div(n1, n2):
        """
            div - returns division of n1 over n2
                  returns None if There is a division by zero 
        """
        if n2 == 0:
            print("Invalid Operation : Division By Zero is forbidden")
            return None
        return n1 / n2
    
        
    if operation == "+":
        return sum(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return div(num1, num2)
    else :
        print("Invalid Operation : Run Again")
    