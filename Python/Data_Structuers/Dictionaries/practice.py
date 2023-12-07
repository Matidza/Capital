#Create an Empty dictionary
dic = {}
print("\n1: Empty dictionary")
print(dic, '\n')

#Adding to dic
print("2: Adding to dic")
dic['name'] = "Rex"
dic["clour"] = "White-silver"
dic["legs"] = "age"
print(dic)

#new dictonary
info = {
    "name": "Zwivhuya", "surmane": "Mukwevho","gender": "Male",
    "marital": "Single", "Skills": ["python", "Java Script", "Django", "Data Analytics"],
    "city": "Makhado", "address": {
        "street": "Rixile street, No: 20002",
        "suburb": "Tshikota Location",
        "province": "Limpopo",
        "zip code": "0920",
    }
}
print("\n 3: New dictionary")
print(info, "\n" )
print(len(info))

values = info.values()
keys = info.keys()
print(f"\n keys:{keys}")
print(f"\nValues: {values}")

info["Skills"].append("css")
print(info) 
print(dic.items())


info.popitem()
print(info)
del dic