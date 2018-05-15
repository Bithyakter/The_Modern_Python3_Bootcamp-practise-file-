##urls
import re

# url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
# match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
# print(f"Protocol: {match.group(1)}")
# print(f"Domain: {match.group(2)}")
# print(f"Everything Else: {match.group(3)}")
# print(match.groups())
# print(match.group())
#


###Regex Compilation Flags
# Without Verbose Flag...
# pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

# pattern = re.compile(r"""
# 	^([a-z0-9_\.-]+)	      #first part of email
# 	@					      #single @ sign
# 	([0-9a-z\.-]+)		     #email provider
# 	\.					     #single period
# 	([a-z\.]{2,6})$		     #com, org, net, etc.
# """, re.X | re.I)
#
# match = pattern.search("ThomaS123@Yahoo.com")
# print(match.group())
# print(match.groups())

# ###Symbolic Group Names
# def parse_name(input):
#     name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
#     matches = name_regex.search(input)
#     print(matches.group())
#     print(matches.group('first'))
#     print(matches.group('last'))
#
# parse_name("Mrs. Tilda Swinton")
#
#
#
# ###Redact
# import re
# text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"
#
# pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
# result = pattern.sub("\g<1> \g<2>", text)
# print(result)


###import re
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
titles.sort()
fixed_titles = []

pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    # result = pattern.sub("\g<2> - \g<1>", book)
    result = pattern.sub("\g<date> - \g<title>", book)

    fixed_titles.append(result)
fixed_titles.sort()
print(fixed_titles)

