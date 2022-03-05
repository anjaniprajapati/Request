import requests
import json
def request():
    url_1=requests.get("http://saral.navgurukul.org/api/courses")
    with open("anjani.json","w")as file:
        json.dump(url_1.json(),file,indent=6)
    js_1=url_1.json()
    c=0
    l=[]
    print("Number ------ course -------id")
    for i in js_1["availableCourses"]:
        print(c,i["name"],i["id"])
        l.append(i["id"])
        c+=1
    user_1=int(input("enter couser number-->>"))
    url_2=requests.get("http://saral.navgurukul.org/api/courses/"+(l[user_1])+"/exercises")
    js_2=url_2.json()
    l_1=[]
    c=0
    for i in js_2["data"]:
        print(c,i["slug"])
        l_1.append(i["slug"])
        c+=1
    # print(c,l_1)
    user_2=int(input("enter slug number--->>"))
    url_3=requests.get("http://saral.navgurukul.org/api/courses/"+str(user_1)+"/exercise/getBySlug?slug="+l_1[user_2])
    js_3=url_3.json()
    # print(url_3)
    print("content",js_3["content"]) 


    print(" you want go previous content than enter up")
    print(" you want go next content than enter n ")
    print(" you want go previous content than enter p")
    print(" you want go previous content than enter exit")

    for i in range(len(l_1)):
        # print(i[l_1])
        user_3=input("enter your next step--->>")
        if user_3=="up":
            url_3=requests.get("http://saral.navgurukul.org/api/courses/"+str(user_1)+"/exercise/getBySlug?slug="+l_1[user_2-1])
            js_3=url_3.json()
            print(user_2-1,"content",js_3["content"])
        if user_3=="n":
            url_3=requests.get("http://saral.navgurukul.org/api/courses/"+str(user_1)+"/exercise/getBySlug?slug="+l_1[user_2+1])
            js_3=url_3.json()
            print(user_2+1,"content",js_3["content"])
        if user_3=="p":
            url_3=requests.get("http://saral.navgurukul.org/api/courses/"+str(user_1)+"/exercise/getBySlug?slug="+l_1[user_2])
            js_3=url_3.json()
            print(user_2,"content",js_3["content"])
        if user_3=="exit":
            request()


request()