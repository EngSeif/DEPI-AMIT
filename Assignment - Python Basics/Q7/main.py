from funcs import get_coordinates

x_coord, y_coord = get_coordinates()

print(f"The entered coordinates are X: [{x_coord}], Y: [{y_coord}].")

people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("Diana", 28),
    ("Ethan", 22),
    ("Fiona", 31),
    ("George", 27),
    ("Hannah", 29),
    ("Ian", 33),
    ("Julia", 26)
]

for data in people:
    name, age = data
    print(f"{name} is {age} years old.")