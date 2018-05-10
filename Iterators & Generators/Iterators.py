###using next()

'''name = "python"
iter(name)
it = iter(name)
print(next(it))                   ###running until raises a Stop iteration error
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

###example-2
num = [1,2,3,4,5,6]
it = iter(num)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))'''


"""Custom For Loop"""

def my_for(iterable):
    iterator = iter(iterable)
    while True:

        try:
            print(next(iterator))
        except StopIteration:

            print("END OF ITERATOR")

            break
my_for("Hello")

###example-2
def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x*x)

my_for("LOL", print)
my_for([1,2,3,4,5], square)


"""Custom Iterator"""

class counter():
    def __init__(self,low,high):
        self.low = low
        self.high = high

    def __iter__(self):
        return iter("Hi There !")

    # def __iter__(self):                  ###infinite
    #     return self
    # 
    # def __next__(self):
    #     return 1


for x in counter(0,10):
    print(x)


###example-2
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

for x in Counter(50,70):
    print(x)


