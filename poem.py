f=open("t\\text.txt","w")

txt="The first letter is A. The second letter of the alphabet is B. The third letter is C. The fourth letter is D. The first number is one, it has letters. The first letter of the alphabet is A, it has one letter. The fourth number is 4, it has four letters. Addition is a type of math that is able to add numbers."

f.write(txt)
f=open("t\\text.txt","r")
print(f.read())
