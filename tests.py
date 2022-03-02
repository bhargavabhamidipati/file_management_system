from server_functions import *
from work_with_files import *
import unittest


class testing_system(unittest.TestCase):
    """
        a class that is used to test all the commands performed by the
        client server system
    """
    def test_create_folder(self):
        user_obj = User("bhargav")
        result = user_obj.create_folder("test3")
        self.assertEqual(result,"folder created.....")
        result = user_obj.create_folder("test3")
        self.assertEqual(result,"folder already exists")

    def test_write_file(self):
        user_obj = User("bhargav")
        result = user_obj.write_file("test7.txt","hen is  a good boy")
        self.assertEqual(result,"data written")
        result = user_obj.write_file("text7.txt","all day is monday")
        self.assertEqual(result,"data written")

    def test_read_file(self):
        user_obj = User("bhargav")
        result = user_obj.read_file("sample.txt")
        self.assertNotEqual(result,"fail to open file")
        result = user_obj.start_reading()
        self.assertEqual(result,"bhargav are good and want he is doing good you are beautiful ")

    def test_login(self):
        result = login_verify("bhargav","bhargav123")
        self.assertEqual(result,"logged in successfully!!!!!")
        result = login_verify("bhargav","bhargav")
        self.assertEqual(result,"Wrong password or user name!!!!")

    def test_register_user(self):
        result = register_user("sameer","sameer123")
        self.assertEqual(result,"user registered successfully!!!!")
        result = register_user("sameer","sameer123")
        self.assertEqual(result,"username already exists")

if __name__ =='__main__':
    unittest.main()
