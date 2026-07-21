from hello import hello

def main():
    test_hello()


def test_argument():
    hello("Todz") == "Hello, Todz"

def test_default():
    hello() == "Hello, world"
    
if __name__ == "__main__":
    main()