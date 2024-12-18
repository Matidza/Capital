### Creating a Set
### Getting Set's Length

zar = {"What", "Break", "Full", "What-ever",
    'banana', 'orange', 'mango', 'what'}

print(zar)
print(f"The length of the set is: {len(zar)}(8 values)")

### Accessing Items in a Set
#We use loops to access items. We will see this in loop section
### **Checking an Item**

zar = {"What", "Break", "Full", "What-ever",'banana', 'orange', 'mango', 'lemon'}
print("Does the zar set contain: ", "What" in zar)

### Adding Items to a Set

zar = {"What", "Break", "Full", "What-ever",'banana', 'orange', 'mango', 'lemon'}
lt = [12, 254, 78]
zar.add("Can we add a list/another data structure type")
print(zar)
#Add multiple items using _update()_
zar.update(["koilo", "Wrong"])
print(zar)
zar.update(lt)
print(zar)
zar.remove("banana")
print(zar)