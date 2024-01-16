data = (
    "Zwivhuya", "Mukona", "wanga", "Todani,",
    "what","Why", "Pok", "khg",
)
print("The first item:")
print(data[0])

print(len(data) - 1)

#Slicing
print(data[0:5])
print(data[:4])

for i in data:
    print(i)

print(f"\"Zwivhuya\"" in data)


print(data)

lst = list(data)
print(lst)