# utils/test_data_generator.py
from faker import Faker
fake = Faker()
import random
number =  random.randint(1, 100)
class TestData:
    
    @staticmethod
    def valid_email():
        return f"{fake.user_name()}{number}@example.com"
    
    @staticmethod
    def invalid_email():
        """Email tanpa @ dan ."""
        return f"{fake.user_name()}com"

    @staticmethod
    def valid_password():
        return "Test12345!"

    
    @staticmethod
    def first_name():
        return fake.first_name()

    @staticmethod
    def last_name():
        return fake.last_name()


    @staticmethod
    def phone_number():
        return fake.phone_number()

    
    @staticmethod
    def long_text():
        """Text lebih dari batas maximal"""
        return "X" * 33

    @staticmethod
    def long_phone():
        """Text lebih dari batas maximal"""
        return "X" * 33
