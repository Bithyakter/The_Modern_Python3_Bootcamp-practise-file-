import re

pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")


###example-2
pattern = r"a(bc)(de)(f(g)h)i"                                       #Use of group() function
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.groups())



"""Special Group"""
#Format of named group (?P<name>...)
#Format of non-capturing group (?: ...)

pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
print(match.groups())


###example-4
pattern = r"gr(a|e)y"
match = re.match(pattern, "gray")
if match:
    print ("Gray is fine!")
match = re.match(pattern, "grey")
if match:
    print ("Grey is OK also!")
match = re.match(pattern, "griy")
if match:
    print ("No way, what Griy is?!!")




