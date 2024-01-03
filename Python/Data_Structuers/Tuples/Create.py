empty = ()
empty = tuple()
print(f"\nThis is an empty tuple: {empty}")

#tuples with values
tpl = ("Zwivhuya", "wanga", "Miukona")
# print(f"\nTuple with values")
print(tpl)

print(len(tpl))

n = 4
for i in range(n):
    print(tpl)
print(end="")

# Creating an empty tuple
empty = ()
empty = tuple()

# Tuple with initial values
zar = ("What", "Break", "Full", "What-ever")
print(zar, end="")

### Tuple length
zar = ("What", "Break", "Full", "What-ever")
print(len(zar), end="")

### Accessing Tuple Items
zar = ("What", "Break", "Full", "What-ever")
print(f"Accessing Tuple Items: \n{zar[0]} \n{zar[2]}")
print(len(zar) -1)
print(zar[-1])


### Slicing tuples
#- Range of Positive Indexes
zar = ("What", "Break", "Full", "What-ever",
    'banana', 'orange', 'mango', 'lemon')
print(zar[0: 5])
print(zar[1: 5])
print(zar[0:])
print(zar[1:])
zar[0] = "maybe"
print(zar)

zar = ("What", "Break", "Full", "What-ever",
    'banana', 'orange', 'mango', 'lemon')
tpl = ("Zwivhuya", "wanga", "Miukona")
#print(zar + tpl)
zar.union(tpl)


print(zar)
dollar = ()
for i in range(4):
    print(dollar)