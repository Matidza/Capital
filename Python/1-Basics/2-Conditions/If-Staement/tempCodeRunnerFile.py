def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("what is n: "))
        if n > 0:
            break
    return n
def meow(n):
    for i in range(n):
        print("Meow")
main()
