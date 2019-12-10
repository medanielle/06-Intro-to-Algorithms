import re

"""
1. Recognize the following strings: “bat,” “bit,” “but,” “hat,”
“hit,” or “hut.”
"""

# strings = '''
# bat
# bit
# but
# hat
# hit
# hut
# mit
# mat
# nut
# '''
# pattern = re.compile(r'[bh][aiu]t')
# matches = pattern.findall(strings)
# for match in matches:
#     print(match)

"""​
2. Match any pair of words separated by a single space, that is,
first and last names.
"""

# names = '''
# Bat Batterson
# Bit Byte
# But No
# Hat Hatter
# Hit Runner
# Hut Hitchcock
# Mit Mat
# '''
# pattern = re.compile(r'\w+\s\w+')
# matches = pattern.findall(names)
# for match in matches:
#     print(match)

"""
3. Match any word and single letter separated by a comma and
single space, as in last name, first initial.
"""

# names = '''
# Batterson, B
# Byte, B
# No, B
# Hatter, H
# Runner, H
# Hitchcock, H
# Mit Mat
# '''
# pattern = re.compile(r'\w+,\s\w+')
# matches = pattern.findall(names)
# for match in matches:
#     print(match)

"""
4. Match the set of all valid Python identifiers.
​"""

# import keyword

# identifiers = '''
# pattern1
# 1337V@r
# 1var
# Varible_split
# camelCase
# 3camelCase
# 1st
# first
# 2nd
# second
# num1
# num_1
# list
# List
# lists
# dict
# dicts
# Dict
# str
# string
# int
# integer
# float
# float_num
# True
# true
# False
# f@lse
# if
# in
# and
# And
# y1eld
# yield
# Yield
# '''
# keywords = '(' + '|'.join(keyword.kwlist) + ')'
# # print(keywords)
# # (False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)
# pattern = re.compile(r'^(?!' + keywords + r'|\W)[a-zA-Z_]\w+', re.MULTILINE)
# matches = pattern.finditer(identifiers)

# for match in matches:
#     print(match.group(0))

"""
5. Match a street address according to your local format (keep
your regex general enough to match any number of street
words, including the type designation). For example, American
street addresses use the format: 1180 Bordeaux Drive. Make
your regex flexible enough to support multi-word street
names such as: 3120 De la Cruz Boulevard.
​"""

# streets = '''
# 2048 Batterson blvd
# 64 Bit Dr
# 1920 No lane
# 1440 Hatter loop
# 1660 N Runner circle
# 5140 SE Hitchcock St
# 1200 MitMat Dr
# 1180 Bordeaux Drive
# 3120 De la Cruz Boulevard
# '''
# pattern = re.compile(r'(\d+)\s([NSWE]{1,2})?(\s?(\b\w+))+')
# matches = pattern.finditer(streets)
# for match in matches:
#     print(match.group(0))

"""
6. Match simple Web domain names that begin with “www.”
and end with a “.com” suffix; for example, www.yahoo.com.
Extra Credit: If your regex also supports other high-level
domain names, such as .edu, .net, etc. (for example,
www.foothill.edu).
​"""

# urls = '''
# www.yahoo.com
# www.foothill.edu
# www.google.com
# youtube.com
# yahoo.com
# '''

# pattern = re.compile(r'(w{3}\.)(\w+)\.(com|net|edu|org|mil|gov|)')
# matches = pattern.finditer(urls)
# for match in matches:
#     print(match.group(0))

"""
7. Match the set of all valid e-mail addresses (start with a loose
regex, and then try to tighten it as much as you can, yet
maintain correct functionality). Try to break what we did in class 
and improve it.
​"""

# emails = '''
# TestUser@gmail.com
# test.user@school.edu
# test-123-user@this-place.net
# bademail@.com
# '''

# pattern = re.compile(r'[a-zA-Z.0-9-_+]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9]+')
# matches = pattern.findall(emails)

# for match in matches:
#     print(match)

"""
8. Match the set of all valid Web site addresses (URLs) (start
with a loose regex, and then try to tighten it as much as you
can, yet maintain correct functionality).Try to break what we did in 
class and improve it.
"""

# urls = '''
# http://testsite.com
# https://www.google.com
# https://youtube.com
# https://www.nasa.gov
# '''

# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(0))

"""​
9. type(). The type() built-in function returns a type object,
which is displayed as the following Pythonic-looking string:
​
    # >>> type(0)
    # <type 'int'>
    # >>> type(.34)
    # <type 'float'>
    # >>> type(dir)
<type 'builtin_function_or_method'>
​
Create a regex that would extract the actual type name from
the string. Your function should take a string like this <type
'int'> and return int. (Ditto for all other types, such as
‘float’, ‘builtin_function_or_method’, etc.) Note: You
are implementing the value that is stored in the __name__
attribute for classes and some built-in types.
​"""

# types = '''
# <type 'int'>
# <type 'float'>
# <type 'str'>
# <type 'list'>
# <type 'dict'>
# <type 'set'>
# '''

# pattern = re.compile(r'(<(type|class) \')(\w+)\'>')
# matches = pattern.sub(r'\3', types)

# print(matches)
# type2 = pattern.sub(r'\3', str(type(types)))
# print(type2)

"""
10. Processing Dates. In Section 1.2, we gave you the regex pattern
that matched the single or double-digit string representations of
the months January to September (0?[1-9]). Create the regex
that represents the remaining three months in the standard
calendar.
"""

# month_nums = '''
# 1   01
# 2   02
# 3   03
# 4   04
# 5   05
# 6   06
# 7   07
# 8   08
# 9   09
# 10  10
# 11  11
# 12  12
# '''

# pattern = re.compile(r'((0?[1-9]\b)|(1[0-2]))')
# matches = pattern.finditer(month_nums)

# for match in matches:
#     print(match.group(0))

