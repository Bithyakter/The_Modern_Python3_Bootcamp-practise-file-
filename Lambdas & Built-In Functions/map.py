''''
nums = [2,4,6,8]

# doubles =map (lambda x: x*2, nums)

doubles =list(map(lambda x: x*2, nums))

# print(doubles)
for num in doubles:

    print(num)


people = [ "Touhid", "Trisha", "Nitu","Shammi"]

peeps = map(lambda name: name.upper(), people)

print(list(peeps))

for x in peeps:
    print(x)
'''''

'''''
lst = [
    { 'First': 'Touhid', 'Last': 'Bithy' },
    { 'First': 'Trisha', 'Last': 'Nitu' },
    { 'First': 'Shammi', 'Last': 'Monisha' },

]

first_name = list(map(lambda x: x['First'], lst))
print(first_name)

for name in first_name:

     print(name)
'''''
'''lst = [2,4,6]

def num(x):
    return x*2
n = map(num, lst)

print(list(n))

for n in lst:
    print(n)

##try
lst = [
    { 'First': 'Touhid', 'Last': 'Bithy' },
    { 'First': 'Trisha', 'Last': 'Nitu' },
    { 'First': 'Shammi', 'Last': 'Monisha' },
]

def num(x):
    return x['First']

output = map(num, lst)

# print(list(output))
# print(type(output))

for n in output:
    print(n)'''


users = [
    {"username": "A", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "T", "tweets": ["I love my cat"]},
    {"username": "B", "tweets": []},
    {"username": "f", "tweets": []},
    {"username": "h", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "q", "tweets": []}
]
#extract active users using filter:
#
# active_users = list(map(lambda x: x['tweets'], users))
#
# print(active_users)
#
# usernames = list(map(lambda x: x["username"].lower(),users))
# print(usernames)


# usernames = list(map(lambda x: x['tweets'], filter(lambda x: x["username"].lower(), users)))
usernames = list(map(lambda x: x['tweets'], filter(lambda x: x["username"]==x["username"].lower(), users)))
print(usernames)


