import re

pattern = r"Bangla"
result = re.match(pattern, "Bangladesh")
if result:
    print("Match Found!")
else:
    print("No match")

##example-2
pattern = r"Bangladesh"                                                     ###don't forget 'import re'
if re.search(pattern, "There is country named Bangladesh in south asia!"):
    print("Match Found!")
else:
    print("No match")
pattern = r"bangla"                                                                  ##use_findall
print(re.findall(pattern, "Bangladeshi bangla and indian bangla are differnet."))


###example-3
pattern = r"bin"
match = re.search(pattern, "combination")
if match:
    print(match.group())

print(match.start())
print(match.end())
print(match.span())


