'''
names = ["Alu", "Bithy", "apple","gadha","ayna"]

a_names = filter(lambda n: n[0]=='a' or n[0]=='A', names)

print(list(a_names))
print(type(a_names))'''

users = [
    {"username": "A", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "T", "tweets": ["I love my cat"]},
    {"username": "B", "tweets": []},
    {"username": "F", "tweets": []},
    {"username": "H", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "Q", "tweets": []}
]
#extract active users using filter:

active_users = list(filter(lambda u: u['tweets'], users))

print(active_users)

#extract inactive users using filter:

# inactive_users = list(filter(lambda u: not u['tweets'], users))
inactive_users = list(filter(lambda u: len (u['tweets'])==0, users))

print(inactive_users)

# #extract inactive users using list comprehension:
# inactive_users2= [user for user in users if not user["tweets"]]
#
# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(),
                     filter(lambda u: not u['tweets'], users)))
print(usernames)


# # extract usernames of inactive users w/ list comprehension
# usernames2 = [user["username"].upper() for user in users if not user["tweets"]]


##combining map & filter

names = ['Alu','Bithy', 'Sky']

lst =list (map(lambda name: f"Your Instructor is {name}", filter(lambda value: len(value) < 5, names)))

for n in lst:
    print(n)


###Reduce
from functools import reduce

n = [4,3,2,1]

print(reduce(lambda x,y: x*y, n))

strings = [ 'This ', 'is ', 'a ','sentences.']
print(reduce(lambda x, y: x + y, strings))

