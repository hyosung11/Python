# import re

# string = 'search this inside of this text please'

# # print('search' in string)

# # print(re.search('this', string))
# # <re.Match object; span=(17, 21), match='this'>

# a = re.search('this', string)
# # print(a.span())
# # print(a.start())
# # print(a.end())
# print(a.group())

# =================================================================
# import re

# pattern = re.compile('search inside of this text please')
# string = 'search inside of this text please and tell me!'

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# # print(a.group())
# # print(b)
# print(d)

# =================================================================
# Advanced Patterns

# import re

# pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = 'SungOh'
# pattern2 = re.compile(r"[a-zA-Z0-9%$#@]{8,}\d")
# password = 'asdf'

# a = pattern.search(string)
# check = pattern2.fullmatch(password)
# print(check)


# Email Password Validation Exercise
# At least 8 char long
# contains any letters, numbers and $%#@


# ends with a number (not used in production code)
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'SungOh'
pattern2 = re.compile(r"[a-zA-Z0-9%$#@]{7,}[0-9]")
password = 'asdfasdf1'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)
