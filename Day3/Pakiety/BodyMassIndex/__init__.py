"""
This is the BodyMassIndex package.
It provides functionalities for BMI calculation
"""

print("BodyMassIndex __init__.py")

from .calculate import calculate_bmi

__version__ = "1.0"

__all__ = ['calculate_bmi']