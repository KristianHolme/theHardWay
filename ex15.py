
#imports argv from system module
from sys import argv
#assigns arguments to variables
script, filename = argv
#opens the file from the argument and assigns it to a variable
txt = open(filename)
#prints the name of the file
print(f"Here's your file {filename}:")
# prints the file with its read command

print(txt.read())
txt.close()
print("Type the file name again:")
file_again = input('>')

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
