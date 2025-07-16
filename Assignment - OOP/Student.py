from User import User

class Student(User):
    """
    Represents a student user, inheriting from the User class.

    Attributes:
        idx (int): Unique identifier of the user (inherited from User).
        name (str): Name of the user (inherited from User).
        role (str): Role of the user in the system, set as "student".
        borrowed_books (list): List of books borrowed by the user (inherited).
        grade_level (str or int): The academic grade level of the student.

    Methods:
        __init__(name, grade_level):
            Initializes a Student instance with a name and grade level.
        get_role():
            Returns the role of the user as a string ("Student User").
    """

    def __init__(self, name, grade_level):
        """
        Initialize a new Student instance.

        Args:
            name (str): The student's name.
            grade_level (str or int): The academic grade level of the student.
        """
        super().__init__(name, "student")
        self.grade_level = grade_level

    def get_role(self):
        """
        Return the role of the user.

        Returns:
            str: The role string "Student User".
        """
        return "Student User"
