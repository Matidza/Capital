#remove Whtespace from string and capitalize

name = input("What is you name? ").strip().title()

first, last = name.split(" ")


#say hello to user
print(f"Hello, {first}, how you doing this evening my \"friend\"?")