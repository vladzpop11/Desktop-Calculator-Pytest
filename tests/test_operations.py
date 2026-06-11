import pytest
from calculator import Calculator

def test_add_valid():
    calc = Calculator()
    assert calc.add(5, 3) == 8

def test_subtract_valid():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_multiply_valid():
    calc = Calculator()
    assert calc.multiply(7, 3) == 21

def test_divide_valid():
    calc = Calculator()
    assert calc.divide(20, 5) == 4.0

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_square_valid():
    calc = Calculator()
    assert calc.square(5) == 25

def test_square_root_valid():
    calc = Calculator()
    assert calc.square_root(9) == 3.0

def test_square_root_negative_invalid():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.square_root(-1)

def test_power_valid():
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1

def test_history_tracking():
    calc = Calculator()
    calc.add(2, 3)
    calc.multiply(4, 5)
    history = calc.get_history()
    assert len(history) == 2
    assert "ADD" in history[0]
    assert "MULTIPLY" in history[1]

if __name__ == "__main__":
    pytest.main()  # Allows running tests directly