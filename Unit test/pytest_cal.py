import pytest
from cal import square

def main():
    test_square()
    
def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    
    
def test_positive():
    assert square(5) == 25
    assert square(10) == 100
    
def test_negative():
    assert square(-4) == 16
    assert square(-7) == 49

def test_str():
    with pytest.raises(TypeError):
        square("string")

if __name__ == "__main__":
    main()