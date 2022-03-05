import requests
# a=requests.get("http://saral.navgurukul.org/api/courses")
# print(a)








d=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")
print(d.status_code)