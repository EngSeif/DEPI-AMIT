from funcs import ValidNumber

num = 0
num_list = list()

print("Enter 5 Numbers")

# Take 5 Numbers From User
for i in range(5):
    num = ValidNumber(i + 1)
    
    while num == None:
        num = ValidNumber(i + 1)
        
    num_list.append(num)

# Calculate Sum - Average - Maximun- Minimum

sum_n = sum(num_list)
avg_n = sum_n / 5
max_n = max(num_list)
min_n = min(num_list)

# Print Calculation to User

print(f"Summation : {sum_n:>7}")        
print(f"Average   : {avg_n:>7.2f}")        
print(f"Maximum   : {max_n:>7}")        
print(f"Minimum   : {min_n:>7}")
        