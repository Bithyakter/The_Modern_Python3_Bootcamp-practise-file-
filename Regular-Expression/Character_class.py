import re

# A character set containing all vowels
pattern = r"[aeiou]"

# Lets check whether a word got a vowel in it or not

if re.search(pattern, "grey"):
    print("The word 'grey' got at least one vowel!")
else:
    print("No vowel found!")

if re.search(pattern, "qwertyuiop"):
    print("The word 'qwertyuiop' got at least one vowel!")
else:
    print("No vowel found!")

if re.search(pattern, "rhythm myths"):
    print("The word 'rhythm myths' got at least one vowel!")
else:
    print("No vowel found!")



###exmple-2
pattern = r"[A-Z][A-Z][0-9]"                                                      #Numeric digit match
if re.search(pattern, "NS1 is prefix of first name server address."):
# Found NS1 as match
    print("OK")

if re.search(pattern, "You should put a second one with NS2 as prefix."):
# Found NS2 as match
    print("OK")

if re.search(pattern, "I don\'t have any nameserver."):
    print("NS3")
else:
    print("Not OK!")

if re.search(pattern, "PY3K"):
# Found PY3 as match
    print("OK")



###exmaple-3
                                                                        #invert meaning of character class
# Match string that contains NOT ALL Capital letters
pattern = r"[^A-Z]"

if re.search(pattern, "a sentence with all lower case letters."):
    print("Match 1")
if re.search(pattern, "A sentence with mixed English letters."):
    print("Match 2")

if re.search(pattern, "HEADING"):
# All Capital letters
# No Match
    print("Match 3")

if re.search(pattern, "HEADING WITH ALL CAPITAL LETTERS"):
# All Capital letters
# but "spaces" makes it True to NOT ALL Capital
    print("Match 4")

