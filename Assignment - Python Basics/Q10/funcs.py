from re import fullmatch, search
from string import ascii_letters, digits, punctuation

# ================================ Helper Functions =========================================

def isValidUsername(username):
    """
        isValidUsername - check if entered username is Valid
        
        username can contain char and numbers but not numbers only and also no special characters
        
        parameters : 
            - username (string) : username to be checked
             
        return :
            True  : if entered username is Valid
            False : if entered username is NOT Valid
    """
    return fullmatch(r"[a-zA-Z0-9]+", username) is not None and search(r"[a-zA-Z]", username) is not None

def isValidPassword(password):
    """
        isValidUsername - check if entered password is Valid
        
        password is at least 8 in length Must Contain Numbers and Special Character 
        
        parameters : 
            - password (string) : password to be checked
             
        return :
            True  : if entered password is Valid
            False : if entered password is NOT Valid
    """
    if len(password) < 9:
        return False
    
    # check if it contains characters
    isChars  = any(c for c in password if c in ascii_letters)
    
    # check if it contains Numbers
    isNum  = any(c for c in password if c in digits)
    
    # check if it contains Special Characters
    isSpecialChar  = any(c for c in password if c in punctuation)
    
    return isChars and isNum and isSpecialChar

def isUsernameFound(users_dict, username):
    """
        isUsernameFound - check if username is found in the system
        
        parameters : 
            - username (string) : username to be searched for
            - users_dict (dict) : dictionary to search in
             
        return :
            True  : if username is found
            False : if username is NOT found
    """
    for user in users_dict.keys():
        if user == username:
            print("This Username exists please choose another one")
            return True
    return False

# ================================ Main Functions =========================================    

def authenticate(username, password, users_dict):
    """
        authenticate - check if username and its password is correct
        
        parameters : 
            - username (string) : username entered
            - password (string) : password entered
            - users_dict (dict) : dictionary to search in
             
        return :
            True  : if user data is found
            False : if user data is NOT found
    """
    for user in users_dict.keys():
        if user == username:
            if users_dict.get(user, None) == password:
                print("User Authenticated Successfully")
                return True
    return False

def signUp(users_dict):
    """
        signUp - take username and password from user and insert in dictionary
        
        parameters : 
            - users_dict (dict) : dictionary to search in
             
        return : None
    """
    print("\n===== Sign Up =====\n")
    
    # Take Username And Validate Its Rules and Also it is not found in the List
  
    validUsername = False
    validPassword = False
    
    while not validUsername :
        username = input("Enter Your Username :").strip().lower()
        
        # Validate Not Empty
        if username == "":
            print("username cannot be empty")
            continue
    
        # Validate Username Rules
        if not isValidUsername(username):
            print("username can contain char and numbers but not numbers only and also no special characters")
            continue    
        
        # Validate Username is Unique Not Found In the list
        if isUsernameFound(users_dict, username):
            continue    
        
        validUsername = True
            
    
    # Take Password And Validate Its Rules 
    while not validPassword:
        password = input("Enter Your Password :").strip().lower()
        
        # Validate Not Empty
        if password == "":
            print("Password Cannot Be Empty")
            continue
        
        # Validate Password Rules
        if not isValidPassword(password):
            print("password is at least 8 in length Must Contain Numbers and Special Character ")
            continue
        
        validPassword = True

    print("\n===== Successfully Signed Up =====\n")
        
def signIn(users_dict):
    """
        signIn - check if username and its password is in the dict
        
        parameters : 
            - users_dict (dict) : dictionary to search in
             
        return :
            True  : if user data is found
            False : if user data is NOT found
    """
    print("\n===== Sign In =====\n")
    username = input("Enter Your Username :").strip().lower()
    password = input("Enter Your Password :").strip().lower()
    if authenticate(username, password, users_dict):
        print("\n===== Successfully Signed IN =====\n")
    else:
        print("\n===== User Creditials Not True =====\n")
    