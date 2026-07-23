import json
me={
    "name":"firoz",
    "roll_no":32,
    "class":"bca",
    "interest":"web-dev"
}
with open("me.json","w")as file:
    json.dump(me,file,indent=4)
print("done!!!")