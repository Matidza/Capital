# No 1:
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
fruits.count("apple")
print(fruits)
fruits.reverse()
fruits.index('banana')
print(fruits)

#Using Lists as Stacks
stack = [3,4,5]
stack.append(7)
print(stack)
stack.pop()
print(stack)

#Using Lists as Queues
queue = [3,4,5]
queue.append("what")
queue.append("Thas ok")
print(queue)
print(queue.pop(0))
print(queue)

# Deques
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Was that ok")
queue.append("Graham")
queue.popleft()
print(queue)