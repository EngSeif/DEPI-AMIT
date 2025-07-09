# 🎯 Task 5: Simple Inventory System

## 🧠 Concept Focus

**Dictionaries**, ```while``` loop, ```if```/```elif```/```else```, **dictionary methods** (```get```, ```updating values```).

---

## 📄 Description

Create a simple inventory system using a dictionary. The dictionary inventory will store items as keys and their quantities as values (e.g., {'apple': 10, 'banana': 5}).
-   Implement a while loop that continuously prompts the user for an action: add, remove, view, or exit.
- If the user types ```add```: Ask for the item name and quantity to add. Update the inventory.
- If the user types ```remove```: Ask for the item name and quantity to remove. Ensure you don't remove more than available. If removing all, delete the item from the dictionary.
- If the user types ```view```: Print the current inventory (all items and their quantities).
- If the user types ```exit```: Break the loop and end the program


## 💡 Example Output

```
User Simple Inventory System - used to store quantities of each item
Allowed Actions : add, remove, view, exit, 

> Please Enter Your Action : add

*** Add Action ***

> Enter Item Name : orange
> Enter Quantity (Integers Only) : 7
Added orange in inventory Successfully with quantity (7)
> Please Enter Your Action : add

*** Add Action ***

> Enter Item Name : oreo
> Enter Quantity (Integers Only) : 5 
Added oreo in inventory Successfully with quantity (5)
> Please Enter Your Action : view

*** View Action ***


===== User Inventory =====
orange : 7
 oreo : 5



> Please Enter Your Action : remove

*** Remove Action ***

> Enter Item Name : orange
> Enter Quantity (Integers Only) : 10
Item (orange) Has Less Than This Quantity in inventory (7) Cannot Delete
> Please Enter Your Action : remove

*** Remove Action ***

> Enter Item Name : orange
> Enter Quantity (Integers Only) : 5
Item (orange) Updated With new Quantity (2)
Please Enter Your Action : view  

*** View Action ***


===== User Inventory =====
orange : 2
 oreo : 5



> Please Enter Your Action : remove

*** Remove Action ***

> Enter Item Name : oreo
> Enter Quantity (Integers Only) : 5
Item (oreo) Deleted Sucessfully
> Please Enter Your Action : view

*** View Action ***


===== User Inventory =====
orange : 2



> Please Enter Your Action : exit
Closing Program Byeeeeeeeee !
```
