import re

pattern = r"Bangla"
result = re.match(pattern, "Bangladesh")
if result:
    print("Match Found!")
else:
    print("No match")

##example-2
pattern = r"Bangladesh"                                                          #don't forget 'import re'
if re.search(pattern, "There is country named Bangladesh in south asia!"):
    print("Match Found!")
else:
    print("No match")
pattern = r"bangla"                                                                      #use_findall
print(re.findall(pattern, "Bangladeshi bangla and indian bangla are differnet."))


###example-3
pattern = r"bin"
match = re.search(pattern, "combination")
if match:
    print(match.group())                         #return match all string

print(match.start())                             #Index of start & end string
print(match.end())
print(match.span())                              ###Return tuple of index



"""use of . (dot) """
                                                  #character match order
pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "blue"):
    print("Match 3")



"""use of ^ and $ """
                                                 #The start and end of the string can be checked
pattern = r"^wr.te$"
if re.match(pattern, "write"):
    print("Match 1")
if re.match(pattern, "wrote"):
    print("Match 2")
if re.match(pattern, "writer"):
    print("Match 3")


