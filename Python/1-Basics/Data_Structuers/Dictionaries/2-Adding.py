# syntax
#Adding to an existing Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'

dic = {
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

#addding a Key and its Value to an existing dictionary
dic["nick_name"] = "15-11"
dic["Greet" ] = "How you doing"
print(dic["nick_name"])

#Adding a value to an existind dictionary
dic["skills"].append("bash")
dic["skills"].append("Just anything")
print(dic)