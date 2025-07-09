# ================================ Helper Functions =========================================

def checkQuantity():
    """
        checkQuantity - check if Input Quantity is Valid Integer Or Not
        
        parameters : None
             
        return :
            Quantity : if Quantity Number is Valid  
            None     : if Quantity Number is NOT Valid !  
    """
    try:
        q = int(input("Enter Quantity (Integers Only) : "))
        return q
    except ValueError:
        print("Invalid Quantity Entered")
        return None

def print_allowed_actions(user_action_list):
    """
        print_allowed_actions - print allowed user actions
        
        parameters : 
            - user_action_list (list) : list contains all allowed actions user can do
         
        Output : print Allowed User Actions Seperated by ,    
             
        return : None
    """
    print("Allowed Actions : ", end="")
    for act in user_action_list:
        print(f"{act}, ", end="")
    print("\n")
        
# ================================ Main Functions =========================================

def handle_add_action(user_inventory):
    """
        handle_add_action - handle add action for user by adding item and quantity in dictionarry
        
        parameters : 
            - user_inventory (dict) : dict that represent User Inventory
         
        Output : add item to inventory and print success message   
             
        return : None
    """
    print("\n*** Add Action ***\n")
    item = input("Enter Item Name : ").strip().lower()
    
    q = checkQuantity()
    while q == None:
        q = checkQuantity()
    
    user_inventory[item] = q
    
    print(f"Added {item} in inventory Successfully with quantity ({user_inventory[item]})")
    
def handle_remove_action(user_inventory):
    """
        handle_remove_action - handle remove action for user by removing item from inventory if it exists
        
        parameters : 
            - user_inventory (dict) : dict that represent User Inventory
         
        Output : 
            - if item is found :
                    if quantity removed more than available Available :
                        print fail message
                    if quantity removed equals Available :
                        remove item from inventory and print success message
                    if quantity removed more than Available :
                        remove update quantity and print success message
            - if NOT found     : print fail message
             
        return : None
    """
    print("\n*** Remove Action ***\n")
    item = input("Enter Item Name : ").strip().lower()
    q = checkQuantity()
    while q == None:
        q = checkQuantity()
    
    available = user_inventory.get(item, None)

    if available == None:
        print("Item Not Found, Cannot Be Deleted")
    else:
        if available < q:
            print(f"Item ({item}) Has Less Than This Quantity in inventory ({available}) Cannot Delete")
        elif available == q :
            # del user_inventory[item] is Valid Also
            user_inventory.pop(item, None)
            print(f"Item ({item}) Deleted Sucessfully")
        else :
            user_inventory[item] -= q
            print(f"Item ({item}) Updated With new Quantity ({user_inventory[item]})")
        
def handle_view_action(user_inventory):
    """
        handle_view_action - handle view action for user by printing all items from inventory
        
        parameters : 
            - user_inventory (dict) : dict that represent User Inventory
         
        Output : 
            - if empty : print Empty Message
            - if NOT   : print Each Item and its quantity each in a new line
             
        return : None
    """
    print("\n*** View Action ***\n\n")
    
    print("===== User Inventory =====")
    
    if len(user_inventory) == 0:
        print("Empty Inventory")
    else:
        for key, value in user_inventory.items():
            print(f"{key:>5} : {value}")
        
    print("\n\n")
    