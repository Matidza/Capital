from calculator import square

def main():
    test_cal1()

def test_cal1():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

if __name__ == "__main__":
    main()