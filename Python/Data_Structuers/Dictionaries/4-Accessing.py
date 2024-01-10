# syntax
#Accessing Dictionary iterms
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
print("\n")


dic = {
    'first_name':'Zwivhuya',
    'last_name':'Mukwevho',
    'age':250,
    'country':'Mzansi',
    'is_marred':"Nah",
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(dic['first_name'], dic["age"])
print(dic['skills'][1])


#Accessing iterm by name raises an error
#Use .get()
print(dic.get("first_name "))