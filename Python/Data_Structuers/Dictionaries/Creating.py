#Creating a Dictionary
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


dic = {
    "Name:": "Zwivhuya",
    "Surname:": "Mukwevho",
}
print(dic)

#print the key and its values
def v():
    for i in dic:    
        print(f"\n", i, dic[i] ) #this prints the dic's Key and values
v()    