import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools
import logging


# Create a logger
logger = logging.getLogger('my_logger') # w praktyce bardzo czesto korzystamy z getLogger(__name__)
logger.setLevel(logging.WARNING)

# Create a file handler
file_handler = logging.FileHandler('my_log_file.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)




def log_errors(funkcja):
    @functools.wraps(funkcja)
    def wrapper(*args, **kwargs):
        try:
            logger.info(f'Arguments for call {funkcja.__name__} ({args}, {kwargs})')
            funkcja(*args, **kwargs)
        except ValueError as e:
            logger.error(f'Error message {e}')
        except IOError as e:
            logger.warning(f'IOError with following message {e}')
        except Exception as e:
            logger.warning(f'Unknown error {e}')

    return wrapper


@log_errors
def do_opakowania(x : int):
    if x == 10:
        raise ValueError("Dla 10 nie dzialam")
    if x == 5:
        raise IOError("blad polaczenia")
    return x



if __name__ == '__main__':
    do_opakowania(5)
    do_opakowania(10)
    do_opakowania(6)


    def limit_calls(max_calls):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if wrapper.call_count >= max_calls:
                    print("Błąd: przekroczono maksymalną liczbę wywołań")
                    return -1
                wrapper.call_count += 1
                return func(*args, **kwargs)

            wrapper.call_count = 0
            return wrapper

        return decorator

    @limit_calls(max_calls=3)
    def greet(name):
        print(f"Cześć, {name}!")

    greet("Karolina")
    greet("Przemysław")
    greet("Julia")
    greet("Wojtek")



    def add_method_decorator(cls):
        # Define a new method to be added
        def new_method(self):
            return "This is a new method"

        # Add the new method to the class
        cls.new_method = new_method
        return cls


    # Apply the decorator to the class
    @add_method_decorator
    class MyClass:
        def __init__(self, value):
            self.value = value

        def display_value(self):
            return f"The value is {self.value}"


    # Create an instance of the class
    instance = MyClass(10)
    # Call the original method
    print(instance.display_value())  # Output: The value is 10
    # Call the new method added by the decorator
    print(instance.new_method())  # Output: This is a new method



    # https://realpython.com/primer-on-python-decorators/#more-real-world-examples
    # https://refactoring.guru/pl/design-patterns/catalog
    # https://github.com/lord63/awesome-python-decorator
