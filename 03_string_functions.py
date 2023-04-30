story ="once upon a time , there was a programmer named Sahil Garg"
s1 = 'amaama RhokHo MY nAME'

#String Functions

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

