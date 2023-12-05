#creating a list
Var = []
print("Blank Var: ")
print(Var,"\n")

#number list
Lists = [12, 1, 23, 3, 5, 9]
print("This is a number list: ")
print(Lists, "\n")

#list iterms form list
print("Iterm from list:")
print(Lists[0],"\n", Lists[-2])

#string list
Names = [
    "Zwivhuya", "Wanga", "Mukona",
    "todani", "Zwoitwaho", "Who else?"
]
print("\nString list: ")
print(Names)
print("\nIterm from String list:")
print(Names[0])
print(Names[:3])

#Multi-dimentional list
Name = [
    [12, 45, 60 ],
    ["Zwivhuya", "Wanga", "Mukona",
    "todani", "Zwoitwaho", "Who else?"]
]
print("\nMulti-dimentional list: ")
print(Name[0][1])  #Select index 0 list, print index 1 iterm from said list
print(Name[1][0])  #Select index 1 list, print index 0 iterm from said list

#Size if list
List1 = [14, 52, 54, 32, 1]
print("\n Size if list:")
print(len(List1))

#taking inputs
string = input("Enter elements (Space-Seperated): ")
lst = string.split()
print("the list is: ", lst)

#Maping your own list
#n = int(input("\nEnter the size of list: "))
#ls  = list(map(int(input("Enter the elements: " ).strip().split())))[:n]
#print("The List is: ", ls)

hey = []
for i in range(0, 5):
    hey.append(i)
print(hey)

h = ["kbjgk", "jbjhg"]
hey.append(h)
print(hey)
hey.reverse()
hey.insert(-1, "What r u Doing")
print(hey)

print("\n")
a = [ 1, 2.3,4]

len(a)


#Swap
Li = [12, 1, 23, 3, 5, 9]
Li[0], Li[-2] = Li[-2], Li[0]
print(Li)