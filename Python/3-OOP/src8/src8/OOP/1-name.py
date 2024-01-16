def main():
    name = get_name()
    last = get_last()
    print(f"{name} from {last}")

def get_name():
    return input("Name: ")

def get_last():
    return input("last: ")

if __name__ == "__main__":
    main()



