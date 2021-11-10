"""Testing the Calculator"""
from calculator.main import Calculator
from calculator.operations.addition import Addition
from calculator.operations.subtract import Subtract
from calculator.operations.multiply import Multiply
from calculator.operations.divison import Divison
def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Addition.add_number(1,2) == 3

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Subtract.sub_number(3,2) == 1

def test_calculator_multiply():
    """Testing the subtract method of the calculator"""
    assert Multiply.multi(2,2) == 4
def test_calculator_divide():
    """Testing Divide method of calc"""
    assert Divison.divide(4,2) == 2
