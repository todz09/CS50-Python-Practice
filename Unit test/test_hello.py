from hello import hello

def main():
    test_hello()


def test_hello():
    hello("Todz") == "Hello, Todz"
    
if __name__ == "__main__":
    main()