from myproject.main import signature
import pytest


@pytest.mark.parametrize("number, expection", [(10, 1), (-1232.456, -1), (0, 0)])
class TestClass:
    def test_signature(self, number, expection):
        assert signature(number) == expection
