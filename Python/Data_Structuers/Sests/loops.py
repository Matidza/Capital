def Var():
    var = set()
    for i in range(1, 6):
        var.add(i)
    print(var)
Var()

print("\n")

def Sets():
    set1 = set()
    set2 = set()
    for i in range(1,6):
        set1.add(i)
    for i in range(5, 9):
        set2.add(i)
    set3 = print(set1.intersection(set2))
    return set3

Sets()

##
set1 = set()
set2 = set()

for i in range(1,6):
    set1.add(i)
for i in range(5, 9):
    set2.add(i)
set3 = set1.intersection(set2)
print(set3)

what = {12, 25, 45}
print(what)

print(len(what))
if what > set3:
    print("ok")
else:
    print("k")
print(".difference()")
print(set3 - what)

#last

def update():
    lst = [12, 45, 32, 78]
    lts = ["what", "Why"]
    set1 = set(lst)
    set2 = set(lts)
    set1.update(set2)
    print("\n.update()")
    print(set1)
    dick = input({12: "where", 77: 'seven',})
    set1.update(dick)
    print(set1)