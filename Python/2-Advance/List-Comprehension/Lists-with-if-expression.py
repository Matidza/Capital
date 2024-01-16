numbers = [i for i in range(21) if i % 2 ==0]
print(numbers)

odd_numbers = [odd for odd in range(21) if odd % 2 != 0]
print(odd_numbers)

#Filtering
numbers = [-1, -12, -3, -5, 2, 23,3, 4, 5, 6, 7, 8, 9, ]
positive = [i for i in range(21) if i % 2 ==0 and  i >0]
print (positive)

add = [-1, -2, -3, -4, 5, 1, 2, ]
negative = [minus for minus in range(21) if minus % 2 ==0 and minus < 0 ]
print(negative)