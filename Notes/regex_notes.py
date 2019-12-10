# Regular Expresions or RegEx

import re


def get_raw_str():
    print('\t')
    print(r'\t')

# get_raw_str()

#compile() will allow us to separate our pattern matches into a variable that makes it easier to reuse our variable
text_to_match = """Daniel 1234 abcd"""
def get_compile():
    pattern = re.compile(r'1234')
    match = pattern.match(text_to_match)
    print(match)

    # (r'1234') = None, since it isn't at begining

# get_compile()

# match()   *** same as carrot ^ (or anchor) ***
# determines if the regex matches at the begining of the string returns None if its not at the begining, same as ^ anchor

def getmatch():
    my_string = ('Tkinter is the best GUI library out there')
    patter = re.compile('Tkinter')
    my_match = patter.match(my_string)
    print(my_match)

#getmatch()

# search lets us search the entire string ( can use with ^)
def get_search():
    pattern = re.compile(r'Daniel')
    search_item = pattern.search(text_to_match)
    print(search_item)

# get_search()

# finditer()

def get_finditer():
    pattern = re.compile(r'abcd')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)

# get_finditer()

############### META CHARACTERS #################

# . - Any character except a new line
def get_any():
    pattern = re.compile(r'.')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)

#get_any()

text_to_match = """Daniel 1234 abcd this.thing@email.com
"""

def get_any_escape():
    pattern = re.compile(r'\.')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)

# get_any_escape()

# \d - finds any digit (0-9)
def get_any_digit():
    pattern = re.compile(r'\d')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)

# get_any_digit()

# \D - finds any digit (0-9)
def get_non_digit():
    pattern = re.compile(r'\D')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)
# shows special character, new lines, etc
# get_non_digit()

text_to_match = """Daniel 1234 abcd this.thing@email.com
this_other-thing@mail.com
"""
# \w - finds any word character (a-z, A-Z, 0-9, _)
def get_word_char():
    pattern = re.compile(r'\w')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)
# doesn't show hyphens(-), or most punctuation
# get_word_char()

# \W - finds any NON word character (not these: a-z, A-Z, 0-9, _)
def get_non_word_char():
    pattern = re.compile(r'\W')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)
# shows spaces, newlines, and punctuation
#get_non_word_char()


text_to_match = """Daniel 1234 abcd         \tthis.thing@email.com
        this_other-thing@mail.com
"""

# \s - finds any Whitespace (space, tab, new line)
def get_whitespace():
    pattern = re.compile(r'\s')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)
# shows spaces, newlines, and punctuation
# get_whitespace()

# \S - finds any NON Whitespace ()
def get_non_whitespace():
    pattern = re.compile(r'\S')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)
# different from \w in that it shows punctuation
# get_non_whitespace()


# **************** Anchors *****************
# Anchors don't match chars, match invisible positions before or after chars

text_to_match = """Daniel 1234 abcd this.thing@email.com
    this_other-thing@mail.com

    lol lololol 
"""


# \b - finds word boundaries ()
def get_boundaries():
    pattern = re.compile(r'\blol')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)            # <re.Match object; span=(73, 76), match='lol'><re.Match object; span=(77, 80), match='lol'>
# shows things that match 'lol' that are after a space, \n or \t
# get_boundaries()


# \B - finds non-word boundaries ()
def get_non_boundaries():
    pattern = re.compile(r'\Blol')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                # <re.Match object; span=(79, 82), match='lol'>
# shows things that match 'lol' that are after a space, \n or \t
# get_non_boundaries()


# ^ - finds matches at the begining of the string
def get_carrot():
    pattern = re.compile(r'^Dan')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                # <re.Match object; span=(0, 3), match='Dan'>
# 
#get_carrot()

# $ - finds matches at the end of the string
def get_end_str():
    pattern = re.compile(r'lol $')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                # <re.Match object; span=(81, 85), match='lol '>
# 
# get_end_str()
text_to_match = """lol lololol 
Daniel 1234 abcd 
this.thing@email.com
    this_other-thing@mail.com
210-444-4444
512*888*8888
    
"""
def search_3_digit():
    pattern = re.compile(r'\d\d\d-')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #<re.Match object; span=(82, 86), match='210-'><re.Match object; span=(86, 90), match='444-'>
# 
# search_3_digit()


def search_tele():
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #<re.Match object; span=(82, 94), match='210-444-4444'><re.Match object; span=(95, 107), match='512*888*8888'>
# 
# search_tele()

# []  Character Set, used to search a group of characters 

def search_char_set_tele():
    pattern = re.compile(r'\d\d\d[-*]\d\d\d[-*]\d\d\d\d')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #<re.Match object; span=(82, 94), match='210-444-4444'><re.Match object; span=(95, 107), match='512*888*8888'>
# 
#search_char_set_tele()


text_to_match = """lol lololol 
Daniel 1234 abcd 
this.thing@email.com
    this_other-thing@mail.com
800-444-4444
900*888*8888
    
"""
def search_char_set_specific_tele():
    pattern = re.compile(r'[89]00[-*]\d\d\d[-*]\d\d\d\d')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #<re.Match object; span=(95, 107), match='900*888*8888'><re.Match object; span=(82, 94), match='800-444-4444'>
# 
# search_char_set_tele()

def char_set_range():
    pattern = re.compile(r'[a-d]')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #note "D" wasn't found
    
#char_set_range()

def char_set_range_pipe():
    pattern = re.compile(r'[a-d]|[A-D]')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #now is was with |[A-D]
    
#char_set_range_pipe()

def char_set_range_num():
    pattern = re.compile(r'[1-7]')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #no 0s or 8/9
    
# char_set_range_num()

# carrot in char set means opposite
# [^] - carrot is a set negate what you are looking for
def char_set_range_carrot():
    pattern = re.compile(r'[^a-zA-z]')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #
    #<re.Match object; span=(106, 107), match='8'><re.Match object; span=(107, 108), match='\n'><re.Match object; span=(108, 109), match=' '>
#char_set_range_carrot()


text_to_match = """lol lololol 
Daniel 1234 abcd 
this.thing@email.com
    this_other-thing@mail.com
800-444-4444
900*888*8888
cat mat bat pat
    
"""
# match cat, mat, pat, but not bat
def char_set_range_not():
    pattern = re.compile(r'[^b]at')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                #
    #<re.Match object; span=(106, 107), match='8'><re.Match object; span=(107, 108), match='\n'><re.Match object; span=(108, 109), match=' '>
#char_set_range_not()

# ************************** QUANITFIERS ************************

def search_tele_quan():
    pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                # <re.Match object; span=(82, 94), match='800-444-4444'><re.Match object; span=(95, 107), match='900*888*8888'>
# 
# search_tele_quan()

def search_tele_quan_test():
    pattern = re.compile(r'(\d{3}.){3}')
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                # <re.Match object; span=(82, 94), match='800-444-4444'><re.Match object; span=(95, 107), match='900*888*8888'>
# 
# search_tele_quan_test()


text_to_match = """lol lololol 
Daniel 1234 abcd 
this.thing@email.com
    this_other-thing@mail.com
800-444-4444
900*888*8888
cat mat bat pat

Mr. Anderson
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
    
"""
# ? - find 0 or 1 match

def search_quan_quest():
    pattern = re.compile(r'Mr\.?')  #'\.' == escaping the period == literal
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                
        # w/o ? => <re.Match object; span=(125, 128), match='Mr.'><re.Match object; span=(170, 173), match='Mr.'>
        # w/ ? => <<re.Match object; span=(125, 137), match='Mr. Anderson'> <re.Match object; span=(138, 146), match='Mr Smith'> <re.Match object; span=(170, 175), match='Mr. T'>
# search_quan_quest()

def search_quan_quest_more():
    pattern = re.compile(r'Mr\.?\s[A-Z]\w*')  #'\.' == escaping the period == literal
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                
        # w/ + => <re.Match object; span=(125, 137), match='Mr. Anderson'><re.Match object; span=(138, 146), match='Mr Smith'>
        # w/ * => <re.Match object; span=(125, 128), match='Mr.'><re.Match object; span=(138, 140), match='Mr'><re.Match object; span=(156, 158), match='Mr'><re.Match object; span=(170, 173), match='Mr.'>
#search_quan_quest_more()

# * - match 0 or more

# () - groups allow us to match several different patterns
# here we can match an "m" then an 'r' or 's' or 'rs'

def search_quan_quest_again():
    pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')  #'\.' == escaping the period == literal
    matches = pattern.finditer(text_to_match)
    
    for match in matches:
        print(match)                
        # ALL THE NAMES LOL
# search_quan_quest_again()

# find emails
email = """ 
TestUser@gmail.com
test.user@school.edu
test-123-user@this-place.net
bademail@.com
"""

def find_emails_first():
    pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
    matches = pattern.finditer(email)

    for match in matches:
        print(match)        #<re.Match object; span=(2, 20), match='TestUser@gmail.com'>

#find_emails_first()

def find_emails_second():
    pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
    matches = pattern.finditer(email)

    for match in matches:
        print(match)        # <re.Match object; span=(2, 20), match='TestUser@gmail.com'><re.Match object; span=(21, 41), match='test.user@school.edu'>

#find_emails_second()

def find_emails_third():
    pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(com|edu|net)')
    matches = pattern.finditer(email)

    for match in matches:
        print(match)  # all three

#find_emails_third()

def find_emails_mine():
    pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z.0-9-]+\.(com|edu|net)')
    # teach (r'[a-zA-Z.0-9-_+]+@[a-zA-Z.0-9-_]+\.[a-zA-Z.0-9-_]+')
    matches = pattern.finditer(email)

    for match in matches:
        print(match)

# find_emails_mine()

# Groups
urls = """
http://testsite.com
https://www.google.com
https://youtube.com
https://www.nasa.gov
www.website.com
"""

# we can group all of these to grab groups
# group 0 being all groups, then group1 being first group

def find_urls():
    pattern = re.compile(r'(https?://)(www\.)?(\w+)\.(\w+)')
    matches = pattern.finditer(urls)

    for match in matches:
        print(match)

#find_urls()

def find_urls_groups():
    pattern = re.compile(r'(https?://)?(www\.)?(\w+)(\.\w+)')
    matches = pattern.finditer(urls)

    for match in matches:
        print(match.group(0, 1, 2, 3, 4))

# find_urls_groups

def find_urls_groups_sub():
    # substitute function, sub out group 3, 4 for our urls everytime it find a match
    pattern = re.compile(r'(https?://)?(www\.)?(\w+)(\.\w+)')
    subbed_urls = pattern.sub(r'\3\4', urls)
    
    print(subbed_urls)

# find_urls_groups_sub()

# findall() -this returnd matches as a list of strings

def get_find_all():
    pattern = re.compile(r'(Mr|Ms|Mrs)\.?(\s[A-Z]\w*)')  #'\.' == escaping the period == literal
    matches = pattern.findall(text_to_match)
    
    for prefix, name in matches:
        print(f'{prefix}.{name}')                
#get_find_all()

# if there are no groups, it returns matches as a list of strings
# if there is one group,  it returns that group as a list of strings
# if there are two groups, it returns a list of tuples

def get_find_all_ex():
    pattern = re.compile(r'[a-zA-Z.0-9-_+]+@[a-zA-Z.0-9-_]+\.[a-zA-Z.0-9-_]+')  #'\.' == escaping the period == literal
    matches = pattern.findall(email)
    
    for match in matches:
        print(match)

# get_find_all_ex()

# flags   (verbose/multiline, etc
def get_flags():
    string = 'IcAan TyPeE GoOd'
    #pattern = re.compile(r'[aA][oO]')
    pattern = re.compile(r'[ao]', re.IGNORECASE)  # or re.I
    matches = pattern.findall(string)

    for match in matches:
        print(match)

# get_flags()




