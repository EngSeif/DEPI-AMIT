from funcs import print_allowed_actions, handle_add_action, handle_remove_action, handle_view_action

action = ""
user_action_list = ["add", "remove", "view", "exit"]
user_inventory = dict()


print("User Simple Inventory System - used to store quantities of each item")
print_allowed_actions(user_action_list) 

while action != "exit":
    action = input("Please Enter Your Action : ").strip().lower()
    
    while action not in user_action_list:
        print("\nInvalid Input")
        print_allowed_actions(user_action_list)
        action = input("Please Enter Your Action : ").strip().lower()
        
    if action == "add":
        handle_add_action(user_inventory)
    elif action == "remove":
        handle_remove_action(user_inventory)
    elif action == "view":
        handle_view_action(user_inventory)
    elif action == "exit":
        print("Closing Program Byeeeeeeeee !")
        