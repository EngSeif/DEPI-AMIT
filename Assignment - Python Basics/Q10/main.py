from funcs import signUp, signIn

users = {
    'john_doe': 'pass@1234',
    'jane_smith': 'qwerty789!',
    'superuser': 'Admin!2024',
    'guest': 'guest_000',
    'testuser': 'testMe123#'
}

user_actions = ["sign up", "sign in", "exit"]

act = ""

while act != "exit":
    act = input(f"Please Enter Your Action {user_actions} : ").lower().strip()
    
    while act not in user_actions:
        print("\nInvalid Action")
        act = input(f"Please Enter Your Action {user_actions} : ")
        
    if act == "sign up" :
        signUp(users)
    elif act == "sign in":
        signIn(users)
    else:
        pass
        