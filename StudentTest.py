"""
Creator: Daniel Torregroza
Purpose: define the test class to test the Student class and define the specified methods in the test class
Creation date: 12/03/2023

"""


# import the unittest module

import unittest

# import the class Student from the StudentClass file.

from StudentClass import Student

# test the Student class.
class StudentClassTestCases (unittest.TestCase):
     def setUp(self):
         self.studObject = Student("Kim", "Kardashian", "Masters of Business Management", 3.5)

     def tearDown(self):
          del self.studObject
     def test_object_created_required_attributes(self):

          stud = Student("Kim", "Kardashian", "Masters of Business Management")
          self.assertEqual(stud.last_name, "Kim")
          self.assertEqual(stud.first_name, "Kardashian")
          self.assertEqual(stud.major, "Masters of Business Management")
          self.assertEqual(stud.gpa, 0.0)

     def test_object_created_all_attributes(self):

          stud = Student("Kim", "Kardashian", "Masters of Business Management", 3.5)
          self.assertEqual(stud.last_name, "Kim")
          self.assertEqual(stud.first_name, "Kardashian")
          self.assertEqual(stud.major, "Masters of Business Management")
          self.assertEqual(stud.gpa, 3.5)
     def test_student_str(self):
          self.assertEqual(str(self.studObject),
                     "Kim, Kardashian has major Masters of Business Management with gpa: 3.5")
     def test_object_not_created_error_last_name(self):
          with self.assertRaises(TypeError):
               stud = Student(fname=self.studObject.first_name, major=self.studObject.major, gpa=self.studObject.gpa)
     def test_object_not_created_error_first_name(self):
          with self.assertRaises(TypeError):
               stud = Student(lname=self.studObject.last_name, major=self.studObject.major, gpa=self.studObject.gpa)
     def test_object_not_created_error_major(self):
          with self.assertRaises(TypeError):
               stud = Student(lname=self.studObject.last_name, fname=self.studObject.first_name, gpa=self.studObject.gpa)


     def test_object_not_created_error_gpa(self):

          with self.assertRaises(ValueError):
               stud = Student(lname=self.studObject.last_name, fname=self.studObject.first_name, major=self.studObject.major, gpa=-4.5)

          with self.assertRaises(ValueError):
               stud = Student(lname=self.studObject.last_name, fname=self.studObject.first_name, major=self.studObject.major, gpa=4.5)

          with self.assertRaises(TypeError):
               stud = Student(lname=self.studObject.last_name, fname=self.studObject.first_name, major=self.studObject.major, gpa="4.5")
     def test_isinstance_of_gpa(self):
          # test cases to test for isinstance
          self.assertIsInstance(self.studObject.gpa, float)
     # test cases to test the range
     def test_range_of_gpa(self):
          self.assertGreaterEqual(self.studObject.gpa, 0.0)
          self.assertLessEqual(self.studObject.gpa, 4.0)

# main execution
if __name__ == '__main__':
     # Define two Student objects
     studObj1 = Student("Jose", "Rodriguez", "Crossing the Wall", 4.0)
     studObj2 = Student("Jobs", "Steve", "The Best Fruit", 3.5)


     # gets invoked.
     print(studObj1)
     print(studObj2)

     # test all the test cases
     unittest.main()