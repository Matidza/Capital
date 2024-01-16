people = {1, 21, 254}
print(people)

var = set([12, 1254, 2365])
print(var)
var.add("op")
print(var)

for i in range( 6):
    people.add(i)
print(people)

what = people.union(var)
print("\n.union()")
print(what)

v = ({12, 254, 658, 789})
print(v)
v.add('12325')
print(v)


set1 = set()
set2 = set()

for i in range(1,6):
    set1.add(i)
for i in range(5, 9):
    set2.add(i)
set3 = set1.intersection(set2)
print(set3)
