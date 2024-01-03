from calculator import square

def main():
    test_cal()

    
def test_cal():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
    
if __name__ == "__main__":
    main()