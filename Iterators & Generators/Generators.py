"""Basically generator is a quick and easy short way of creating iterators"""
"""Every generator is an iterator but not every iterator is a generator."""

'''def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter =  count_up_to(5)
print(next(counter))
print(next(counter))


"""help(counter)"""                   ##document

counter =  count_up_to(12)
for num in counter:
    print(num)'''


# Lame function that returns a list of beats.
# Only runs 100 times
"""writing a Beat Making Generators"""

def current_beat():
    max = 100
    nums = (1,2,3,4)
    i = 0
    result = []
    while len(result) < max:
        if i >= len(nums): i = 0
        result.append(nums[i])
        i += 1
    return result

print(current_beat())


# Infinite Generator - returns one beat a time, no list used!
def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1

counter = current_beat()
print(next(counter))
print(next(counter))

# for n in counter:           ###infinite
#     print(n)




"""Testing Memory Usage With Generators"""

def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a+b
    return nums

print(fib_list(10))


# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1


for n in fib_gen(1000000):
    print(n)

# for n in fib_gen(10):
#     print(n)

