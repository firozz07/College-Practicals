import json
me={
    "name":"firoz",
    "roll_no":32,
    "class":"bca",
    "interest":"web-dev"
}
new_string=json.dumps(me,indent=2)
print(new_string)
