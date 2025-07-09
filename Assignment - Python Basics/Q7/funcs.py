# ================================ Helper Functions =========================================

def checkFloatNum(cord) :
    """
        checkFloatNum - check if entered Number is a Valid Float
        
        parameters : 
            - cord (string) : cord to be taken as an input
             
        return :
            coordinate : if Number is a Valid Float
            None       : if Number is a NOT Valid Float
    """
    try:
        coordinate = float(input(f"Enter {cord} Coordinate : "))
        return coordinate
    except ValueError:
        print("Invalid Value Entered")
        return None
    
# ================================ Main Functions =========================================

def get_coordinates():
    """
        get_coordinates - get point coordinates from User 
        
        parameters : None
             
        return : (x, y) "Coordinates Tuple"
    """
    x = checkFloatNum("X")
    while x == None:
        x = checkFloatNum("X")
        
    y = checkFloatNum("Y")
    while x == None:
        x = checkFloatNum("Y")

    return (x, y)
    