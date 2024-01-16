def insertion_sort(arr):
    for i in range(1, len(arr)):
            j = i
            while arr[j -1] > arr[j] and j > 0: #swapping condition
                  arr[j-1], arr[j] = arr[j], arr[j-1] #Swapp
                  j -= 1

arr = [2, 6, 5, 1, 7, 9, 4, 8, 3,0]
insertion_sort(arr)
print(arr)

#arr = [2, 6, 5, 1, 7, 9, 4, 8, 3]
#print(sorted(arr))