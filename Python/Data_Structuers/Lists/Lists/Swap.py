Var = [12, 35, 9, 56, 24]
Var.reverse()
print(Var)
Var.insert(5, 100)
print(f"{Var}\n")


def swap(newlist):
    size = len(newlist)

    #Swapping
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size -1] = temp

    return newlist

newlist = [12, 35, 9, 56, 24]
print(swap(newlist), "\n")

def swapping(new):
    #swapppimg
    new[0], new[1] = new[1], new[0]
    return new
new = [1, 2, 3, 4, 5]
print(swapping(new),"\n")

def swapList(list):
     
    first = list.pop(0)   
    last = list.pop(-1)
     
    list.insert(0, last)  
    list.append(first)   
     
    return list
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))