#1
tup = ()
print("\n1: empty tuple")
print(tup)

#2
brothers = ("Zwivhuya", "Todani",)
sisters = ("mukona", "wanga")
print(f"2: tuple: ")
print(f"brothers: {brothers}")
print(f"sisters: {sisters}")

#3
siblings = brothers + sisters
print(f"\nJoin the two tuple")
print(siblings)

print(f"\nLength of tuple is: ")
print(len(siblings))

parents = ("mom", "dad")
family = parents + siblings
print(family)