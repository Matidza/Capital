import json


student_json = '''{
    "Name": "Zwivhuya", "Surname": "Mukwevho",
    "Town": "Makhado", "Skills": ['Python', 'JavaScript', 'Django'],
}'''


person_dic = json.loads(student_json)
for person in person_dic:
    print(person)