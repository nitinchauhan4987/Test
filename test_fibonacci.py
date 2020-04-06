from fibonacci import fib


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1


def test_fib1():
    assert fib(10) == 55


def test_fib2():
    assert fib(11) == 89
