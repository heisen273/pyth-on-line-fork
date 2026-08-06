

def slow_fibonacci(n):
    if n < 2:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)


def test_my():
    a = 1
    b = 445444
    c = 3
    assert a == 1
    pass

    # Slow code here: takes 5seconds to run
    slow_fibonacci(39)
