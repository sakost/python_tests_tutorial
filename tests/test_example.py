import myproject


def test_example(mocker):
    mocked_func = mocker.patch('myproject.main.signature')
    mocked_func.return_value = 'mocked'

    assert myproject.main.signature(1) == 'mocked'
