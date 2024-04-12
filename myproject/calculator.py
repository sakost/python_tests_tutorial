class Calculator:
    """
    Calculator class
    """
    def add(self, a: float, b: float) -> float:
        """
        Adding two numbers
        :param a:
        :param b:
        :return: Sum of two numbers: float
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtracting two numbers
        :param a:
        :param b:
        :return: Difference of two numbers: float
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiplying two numbers
        :param a:
        :param b:
        :return: Product of two numbers: float
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Dividing two numbers
        :param a:
        :param b:
        :return: Division of two numbers: float
        """
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
