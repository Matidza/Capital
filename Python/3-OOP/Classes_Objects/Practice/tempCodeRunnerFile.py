#!/usr/bin/python3

class square:
    def __init__(self, size= 0):
        self.size = size
        try:
            if not isinstance(size, int):
        except TypeError:
            print("size must be an integer")
        
        try:
            if size < 0:
        except ValueError:
            print("size must be >= 0")

p = square()
print(square())