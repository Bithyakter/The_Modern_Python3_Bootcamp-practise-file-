import re

pattern = r"(.+) \1"
match = re.match(pattern, "word word")                      #use of \
if match:
    print ("Match 1")
match = re.match(pattern, "?! ?!")
if match:
    print ("Match 2")
match = re.match(pattern, "abc cde")
if match:
    print ("Match 3")


#example-2

pattern = r"(\D+\d)"                                       #\d = Digit
match = re.match(pattern, "Hi 999!")                       #\s = whitespace
if match:                                                  #\w = word character
    print("Match 1")
match = re.match(pattern, "1, 23, 456!")                   #\D = without Digit
if match:
    print("Match 2")
match = re.match(pattern, " ! $?")
if match:
    print("Match 3")




#example-3

pattern = r"\b(cat)\b"                                      #\A & \Z = Match start & end of the string
match = re.search(pattern, "The cat sat!")
if match:                                                   #\b = Limit of the word
    print ("Match 1")
match = re.search(pattern, "We s>cat<tered?")
if match:
    print ("Match 2")
match = re.search(pattern, "We scattered.")
if match:
    print ("Match 3")
match = re.search(pattern, "We/cat.tered.")
if match:
    print ("Match 4")
match = re.search(pattern, "We{cat!tered.")
if match:
    print ("Match 5")



