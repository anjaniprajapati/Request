dict={}
dict["data1"]={
    "name":"Anjnai",
    "class":11,
    "Age":17,
    "phone no":8470869987,
}
dict["data2"]={
    "name":"Ranjani",
    "class":10,
    "Age":15,
    "phone":7275675442
}
import json
py=json.dumps(dict,indent=6)
with open("data.json","w") as f:
    f.write(py)
f1=open("data.json","r")
s=f1.read()
print(s,type(s))

# dict1=json.loads(s)
# print(dict1)

    