"""
Creator: Daniel Torregroza
Purpose: define the test class to test the Student class and define the specified methods in the test class
Creation date: 12/03/2023

"""

class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):


        # creation, raise an exception.
        if lname == None:
            raise Exception("__init__() missing 1 positional argument: 'lname'.")

        # otherwise, initialize the instance variable last_name with lname
        else:
            self.last_name = lname


        # creation, raise an exception.
        if fname == None:
            raise Exception("__init__() missing 1 positional argument: 'fname'.")


        else:
            self.first_name = fname


        # creation, raise an exception.
        if major == None:
            raise Exception("__init__() missing 1 positional argument: 'major'.")
        else:
            self.major = major


        if isinstance(type(gpa), float):
            raise Exception("The  positional argument 'gpa' is not a float value.")

        # Condition to check if the gpa is not in the range of 0 - 4 inclusively.
        # If it is not in range, the raise a ValueError.
        elif gpa < 0.0 or gpa > 4.0:
            raise ValueError("The positional argument 'gpa' is not valid.")
        else:
            self.gpa = gpa

    # method must return a string  of the Student details.
    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
