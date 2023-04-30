story ="once upon a time , there was a programmer named Sahil Garg"
s1 = 'amaama RhokHo MY nAME'

#String Functions
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', 
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 
'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
'translate', 'upper', 'zfill']
'''


print(len(story)) # returns the number of character in string
print(story.endswith("Garg")) # Return true if the string ends with Mentioned word
print(story.count("a")) # counts the times of character/string occuring.
print(story.find("Sahil")) # find the provided word and return the index of first occurence , if not found , returns -1
print(story.replace("Sahil","Jahil")) # replace the word for all the occurences
print(s1.capitalize()) # capitalize the first character of the first word and convert all words in small letter
print(s1.casefold()) # converts all character to lowercase, similiar to lower(), Python String casefold() Method is more aggressive in conversion
# to lowercase characters because it tends to remove all case distinctions in a String.
print(s1.center(55)) # takes 2 argument ,first arg is mandatory and should be a number.
#Python String center() Method tries to keep the new string length equal to the given length value and fills the extra characters using the default character (space in this case). 
print(s1.center(55,'$')) # will add '$' and keep the original string in center and fill remaining character with '$'
print(s1.count('Rho',1,20)) # return the number of times a particular value appeared in the string. # 1 and 20 are start and end points which are optional
print(s1.encode('utf-8',errors='ignore')) # encode the string in 





##
