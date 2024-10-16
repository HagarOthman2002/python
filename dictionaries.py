# -*- coding: utf-8 -*-
"""dictionaries.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1icdrmRBab7qO2FmuE3d2Ias8DEYh4n8d

## Dicts
Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

Dictionaries and lists share the following characteristics:
<ul>
    <li>Both are mutable.</li>
    <li>Both are dynamic. They can grow and shrink as needed.</li>
    <li>Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.</li>
</ul>

Dictionaries differ from lists primarily in how elements are accessed:
<ul>
    <li>List elements are accessed by their position in the list, via indexing.</li>
    <li>Dictionary elements are accessed via keys.</li>
</ul>

<img src="assets/images/Dictionary-Key-Value-Pairs-Illustration.png">
"""

l = ["mohamed" , 20 , "eng" , "cairo" , "lfkwoj"]
print(l[2])

d = {
    "name":"bob",
    "age":25,
    "job":"eng",
    "city":"Cairo",
    "email":"lgjeljo"
}
# A value is retrieved from a dictionary by specifying its corresponding key in square brackets
print(d['name'], d['age'])
# you can check how many keys in the dict using len
print(len(d))

"""#### Building a Dictionary Incrementally"""

person = {}
person['fname'] = 'mohamed'
person['lname'] = 'yehia'
person['age'] = 30
person['preferred anime'] = ['black clover', 'hunter', 'attack on titans']
print(person)

person = {"fname":'mohamed' , "lname":"yehia" , "age":30 , "preferred anime":['black clover', 'hunter', 'attack on titans']}

print(person['fname'])

print(person['preferred anime'])
print(person['preferred anime'][1])

person['preferred anime'] = [{'rating':7, 'name':'black clover'},
                             {'rating':9, 'name':'hunter'},
                             {'rating':9, 'name':'attack on titans'}]

print(person)

person['preferred anime'][1]["rating"]

print(person['preferred anime'])
print(person['preferred anime'][1]["rating"])

import requests
import json
api_key = "204c762825b47ea8dd6859fb9e5b344b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=cairo"
response = requests.get(complete_url)
received_dict = response.json()
# the above code is not important
print(received_dict)

print(received_dict['main']['temp']-273)

"""Note:
a dictionary key must be of a type that is immutable like integer, float, string, and Boolean

#### dictionary methods
<ul>
<li>D.clear() -> None.  Remove all items from D.</li>
<li>D.copy() -> a shallow copy of D </li>
<li>D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None</li>
<li>D.items() -> a set-like object providing a view on D's items</li>
<li>D.keys() -> a set-like object providing a view on D's keys</li>  
<li>D.values() -> an object providing a view on D's value</li>  
<li>D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised</li>  
</ul>
"""

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
d.clear()
print(d)

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
print(d.keys())
print(d.values())
print(d.items())

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
poped_email = d.pop("email")
print(poped_email)
print(d)

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
d.pop("klko")
print(d)

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
poped_value = d.pop("klko" , "not existed")
print(poped_value)
print(d)
poped_value = d.pop("age" , "...")
print(poped_value)
print(d)

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
print(d['dddddd'])

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
print(d["age"])
age = d.get("age")
print(age)
number = d.get("phone-number")
print(number)
print(d["phone-number"])

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
s = d.copy()

"""#### check if the key existed in dict"""

d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
if "name" in d:
    print(d['name'])

if "phone-number" not in d:
    d["phone-number"] = "000000000000000000"

print(d)

"""#### iterate over dict"""

#method 1
d = {'name':'Bob', 'age':25, 'job':'dev', 'city':'New York', 'email':'bob@web.com'}
for key in d: # key is just var name you can choose whatever you want
    print(f"the {key} pointed to the value {d[key]}")


print("*" * 20)
#method 2
for key, value in d.items():
    print(f"the {key} pointed to the value {value}")

"""### count words"""

sample = '''A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary, I throw myself down among the tall grass by the trickling stream; and, as I lie close to the earth, a thousand unknown plants are noticed by me: when I hear the buzz of the little world among the stalks, and grow familiar with the countless indescribable forms of the insects and flies, then I feel the presence of the Almighty, who formed us in his own image'''
# put your code here
sample = sample.lower()
words = sample.split(" ")
result = {}
for word in words:
    if word not in result:
        result[word] = 1
    else:
        result[word] = result[word] + 1

splited_words = ["aya" , "ahmed" , "belal" , "magdy" , "karim" , "mohamed" , "mostafa" , "Mark"]

names = ["aya" , "ahmed" , "belal" , "magdy" , "karim" , "mohamed" ,"mohamed", "mostafa" , "Mark"]
# iti

x = ["cat" , "abc"]
x.sort()
print(x)

name = "aya"
print(name[0])

"""Q.5
implement grouped by owner code that

*   accept a dictinary containg file owner name for each file name
*   create a dictionary of containing a list of file names for each owner name in any order


for example if you pass
> files = {
'Input.txt': 'Randy',
'Code.py': 'Stan',
'Output.txt': 'Randy'
}

<br>
as input the output should be

> {'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']}
"""

files = { 'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy' }
{'Stan': ['Code.py'], 'Randy': ['Output.txt', 'Input.txt']}