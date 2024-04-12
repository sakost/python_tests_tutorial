import pytest
from myproject.main import SampleClass
from myproject.calculator import Calculator


@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]


@pytest.fixture(params=[1, 2, 3, 0])
def sample_class_instance(request):
    return SampleClass(request.param)


@pytest.fixture(scope='function')
def calculator_function():
    print("Создание экземпляра Calculator")
    return Calculator()


@pytest.fixture(scope='class')
def calculator_class():
    print("Создание экземпляра Calculator для класса")
    return Calculator()


@pytest.fixture(scope='module')
def calculator_module():
    print("Создание экземпляра Calculator для модуля")
    return Calculator()


@pytest.fixture(scope='session')
def calculator_session():
    print("Создание экземпляра Calculator для сессии")
    return Calculator()

