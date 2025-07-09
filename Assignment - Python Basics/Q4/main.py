from funcs import checkNum, is_prime, is_prime_div_method

num = checkNum()

while num == None:
    num = checkNum()

# Brute Force Version
print("Brute Force Version")

if is_prime(num):
    print("Number is Prime\n")
else:
    print("Number is NOT Prime\n")
    
# Division Method Version
print("Division Method Version")

if is_prime_div_method(num):
    print("Number is Prime\n")
else:
    print("Number is NOT Prime\n")
