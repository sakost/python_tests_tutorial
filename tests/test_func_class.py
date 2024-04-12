from myproject.main import signature


class TestClass:
    def test_signature(self):
        assert signature(10) == 1

    def test_signature2(self):
        assert signature(-1232.456) == -1

    def test_signature3(self):
        assert signature(0) == 0