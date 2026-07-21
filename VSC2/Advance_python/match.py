import re
abt="firoz_pathan"
match=re.search(r"\w+",abt)
if match:
    print("group () example : ", match.group())
    print("span () example : ", match.span())
    print("start () example : ", match.start())
    print("end () example : ", match.end())
else:
    print("No digits found in the string.")