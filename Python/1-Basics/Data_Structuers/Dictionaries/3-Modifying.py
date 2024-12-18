# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

person["first_name"] = "Zwivhuya"
person["age"] = "I don'tknow"
print("\n",person)

for i in  (person):
    print(i)


print("First_name" in person)

#Removing Key and Value Pairs from a Dictionary

#    pop(key): removes the item with the specified key name:
#   popitem(): removes the last item
#   del: removes an item with specified key name

person.pop("age")
print(person)
del person[]
