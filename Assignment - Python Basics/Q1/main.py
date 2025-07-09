from funcs import checkStudentGrade, GradeStudent
     
ans = "y"
Grade = None

while ans == "y":
    # Check Student Grade 
    Grade = checkStudentGrade()
    
    # if Not Valid : propmt to user to enter again
    while Grade == None:
        Grade = checkStudentGrade()
    
    # Print Student Grade
    GradeStudent(Grade)
    
    # See if User Wants to continue or not
    ans = input("Do You Wish To Continue (y/n) : ")
    
    if ans == "n":
        print("Goodbye - Ending Program")
        break

    # Validate Continue answer
    # if not valid prompt user to enter a correct value
    while ans != "y" and ans != "n":
        print("Please Enter A Valid Input (y/n)")
        ans = input("Do You Wish To Continue (y/n) : ")
        
        
        
