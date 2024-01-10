tupl = ()
print("Emty tuple")
print(tupl, "\n")

tup = ("Greek", "Food")
print("Strings in Tuples: ")
print(tup)

lst = [1, 25, 45]
print("\ntuple using list: ")
print(tuple(lst))

Tuple = tuple('Zwivhiuya')
print("\n",Tuple)


tuple = ('hey', 'Wahat')
print(tuple)

Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTupe with mixed Datatypes.")
print(Tuple1)

a = (1,2,35)
Tuple1 = (1,2,43,44)
Tuple2 = ('python', 'programm')
Tuple3 = (Tuple1, Tuple2)
print("\nNested tuple/")
print(Tuple3 + a )

a = (1,2,35)
n = 5
print("\nTuples with loops")
for i in range(int(n)):
    a = (a, )
    print(a)