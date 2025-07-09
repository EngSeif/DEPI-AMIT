
def GradeStudent(grade):
    """
    GradeStudent - Determines and prints the student's letter grade based on their numeric score.

    Parameters:
        grade (int): The student's score (0–100).

    Output:
        Prints the corresponding letter grade:
            - 90–100: A
            - 80–89 : B
            - 70–79 : C
            - 60–69 : D
            - Below 60: F

    Returns:
        None
    """
    
    output = f"Student Grade : "
    if grade >= 90 and grade <= 100 :
        print(output + "A")
    elif grade >= 80 and grade <= 89 :
        print(output + "B")
    elif grade >= 70 and grade <= 79 :
        print(output + "C")
    elif grade >= 60 and grade <= 69 :
        print(output + "D")
    elif grade >= 0 and grade <= 60 :
        print(output + "F")
    else :
        print("Student Grade Is Not Valid Try Again")
        
def checkStudentGrade(): 
    """
    checkStudentGrade - Prompts the user to enter a grade and checks if the input is a valid integer.

    Parameters:
        None

    Returns:
        int: The grade as an integer if the input is valid.
        None: If the input is not a valid integer.
    """

    try:
        score = int(input("Enter Student Grade : "))
        return score
    except ValueError:
        print("Invalid Score - Score Value Must Be Between 0 - 100 Numerical Values Only")
        return None