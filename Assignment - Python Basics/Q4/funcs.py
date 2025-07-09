from math import sqrt, ceil

def checkNum():
    """
        is_prime - check if number is prime or not
        
        parameters : None
             
        return :
            num (int)  : if Number is valid int 
            None : if It is NOT Valid Integer 
    """
    try:
        num = int(input("Enter Number : "))
        return num
    except ValueError:
        print("Invalid Integer Enter Again")
        return None

def is_prime(number):
    """
        ( Brute Force Version )
        is_prime - check if number is prime or not
        
        parameters :
            - number (int) : number to be checked
             
        return :
            True  : if Number is prime 
            False : if Number is NOT prime 
    """
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_prime_div_method(number):
    """
        ( Division Method )
        is_prime_div_method - check if number is prime or not
        
        parameters :
            - number (int) : number to be checked
             
        return :
            True  : if Number is prime 
            False : if Number is NOT prime 
    """
    if number <= 1:
        return False
    for i in range(2, ceil(sqrt(number)) + 1 ):
        if number % i == 0:
            return False
    return True