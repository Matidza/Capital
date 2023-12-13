#Syntax
# [i for i in iterable if expression]

#Examples
# No 1:
print("Example 1:")
language = "Zwivhuya"
lst = list(language)
print(type(lst))
print(lst)

# Or in this format
language = "Zwivhuya"
ls = [i for i in language]
print(ls)

# No:2 
#Using range
la = [i for i in range(1, 10)]
print(la)

numbers = [i for i in range(11) if i >= 1]
print(numbers)

add = [i + i for i in range(11)]
print(add)

power = [i * i for i in range(11)]
print(power)

points = [(i, i * i) for i in range(11)]
print(points)