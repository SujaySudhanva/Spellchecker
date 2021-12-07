#Import TextBlob
from textblob import TextBlob
#Import fileinput
import fileinput
#Import Click (Clear Screen)
import click
  
# Clear Screen using click module
#Def clrscr():
click.clear()

# Using fileinput.input() method
print()
print("Spell check & correction from a text file")
print("____________________________")

for line in fileinput.input(files = 'file1.txt'):
	corrected_word= TextBlob(line).correct()
	print("misspelled_word=", line , "Corrected Word=" , corrected_word )
#print("Corrected Word: ",corrected_word)
print("------------------")
	
