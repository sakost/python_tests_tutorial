from myproject.calculator import Calculator


def test_add(calculator_function: Calculator):
    assert calculator_function.add(2, 3) == 5


def test_subtract(calculator_function: Calculator):
    assert calculator_function.subtract(5, 3) == 2


class TestCalculatorClass:
    def test_multiply(self, calculator_class: Calculator):
        assert calculator_class.multiply(2, 3) == 6

    def test_divide(self, calculator_class: Calculator):
        assert calculator_class.divide(6, 3) == 2


def test_multiply_module(calculator_module: Calculator):
    assert calculator_module.multiply(2, 3) == 6


def test_divide_module(calculator_module: Calculator):
    assert calculator_module.divide(6, 3) == 2


def test_add_session(calculator_session: Calculator):
    assert calculator_session.add(2, 3) == 5


def test_subtract_session(calculator_session: Calculator):
    assert calculator_session.subtract(5, 3) == 2
