"""
By submitting this assignment, we agree to the following:
Aggies do not lie, cheat, or steal, nor tolerate those who do.
We have not given or received any unauthorized aid on this assignment.
Name: Anish Yakkanti
Section: ENGR 102 536
Assignment: Lab7Indie_1
Date: 10-27-23
"""

"""
# PigLatin rules
#If a word starts with a consonant, move the consonants to the end of the word, and add “ay” to the end
#e.g. “computer” becomes “omputercay”
#If a word starts with a vowel, add “yay” on to the end of the word.
#e.g. “engineering” becomes “engineeringyay”
#Note: treat “y” as a vowel for this assignment.
"""

def listToString(s):

	# initialize an empty string
	str1 = ""

	# traverse in the string
	for ele in s:
		str1 += ele

	# return string
	return str1

flag = True # flag to terminate program when stop is entered

while flag == True: # loop to ask for another word
  og_word = str(input("Enter a word to be translated to Pig Latin: ")) #asks user for word  
  if og_word == "stop":
      flag = False 
      print ("Thanks for using this translator!")
  new_word = og_word
  og_list = list(og_word)
  new_list = []
  
  
  if og_list[0] in ["a", "e", "i", "o", "u", "y"]: # tests if vowel is in word
    new_word = og_word + "yay"
    
  else:
    for x in og_list.copy():
       
       if x not in ["a", "e", "i", "o", "u", "y"]:
         new_list.append(x)
         og_list.pop(0) # removes first letter from og list
       else:
         break
       
       new_word = listToString(og_list) + listToString(new_list) + "ay"
  if flag == True: # only prints when flag is true
    print(new_word)


