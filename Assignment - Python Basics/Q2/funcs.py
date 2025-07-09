
def ValidNumber(i):
    """
        ValidNumber - Prompts the user to enter a grade and checks if the input is a valid integer.

        Parameters:
            i - number turn to be inserted

        Returns:
            int: The number as an integer if the input is valid.
            None: If the input is not a valid integer.
    """
    num_exp = ""
    if i == 1:
        num_exp = "st"
    elif i == 2:
        num_exp = "nd"
    elif i == 3:
        num_exp = "rd"
    else:
        num_exp = "th"
        
    try:
        x = int(input(f"Enter {i}{num_exp} Number : "))
        return x
    except ValueError:
        print("You Entered an Invalid Value")
        return None