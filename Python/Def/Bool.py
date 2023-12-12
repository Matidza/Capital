def even():
    x = int(input("What is x: "))
    if is_even(x):
        print("X is even.")
    else:
        print("X is not even")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
even()