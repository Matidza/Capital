from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Was that ok")
queue.append("Graham")
queue.popleft()
print(queue)