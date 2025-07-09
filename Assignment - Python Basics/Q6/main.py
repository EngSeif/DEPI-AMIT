
# Create a list of squares of numbers from 1 to 10 using a list comprehension

squareList = [x ** 2 for x in range(1, 11)]

print(f"Square List of 1 to 10 : {squareList}")

# create a new list containing only the even numbers using a list comprehension

numList = [12, 5, 23, 8, 17, 30]
evenList = [x for x in numList if x % 2 == 0]

print(f"Even List from Num List : {evenList}")

# create a new list containing only the strings that have more than 5 characters, using a list comprehension.

strList = ["apple", "banana", "cherry", "date"]
MoreCharList = [word for word in strList if len(word) > 5]

print(f"List of Strings with more than 5 chars : {MoreCharList}")