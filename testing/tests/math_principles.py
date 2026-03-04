import sys
sys.path.append("../src")

from math_demo import (
add,
add_with_bug
)

def test_addition():
    assert add(2, 2) == 4
    print("Success")

def test_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    assert add_with_bug(1, 1) == 1
    print("Bug")
    #assert add_with_bug(2, 3) == 5

def test_dublicate():
    #тест дублирует себя
    assert add(2, 2) == 2 + 2

def test_overcomplicate():
    #Слишком перегруженный тест
    for i in range(0,2**32):
        for j in range(0,2**32):
            assert add(i, i) == sum(i, j)

def test_reasonadle():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13
    assert add(-6, 7) == 1
    print("Reason")

def test_commutative():
    assert add(2, -2) == 0
    assert add(-2, 2) == 0

if __name__ == "__main__":
    test_addition()
    test_with_bug()
    test_dublicate()
    #test_overcomplicate()
    test_reasonadle()
    test_commutative()