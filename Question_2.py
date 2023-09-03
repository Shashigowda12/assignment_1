#Write a Python program that accepts a word from the user and reverse it.

string=str(input("enter word that need to be reversed"))
revstring=""
for i in reversed(string):
    revstring+=i
print(revstring)