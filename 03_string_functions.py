story ="once upon a time , there was a programmer named Sahil Garg"

#String Functions

print(len(story)) # returns the number of character in string
print(story.endswith("Garg")) # Return true if the string ends with Mentioned word
print(story.count("a")) # counts the times of character/string occuring.
print(story.capitalize()) # capitalize the first character in string 
print(story.find("Sahil")) # find the provided word and return the index of first occurence , if not found , returns -1
print(story.replace("Sahil","Jahil")) # replace the word for all the occurences
