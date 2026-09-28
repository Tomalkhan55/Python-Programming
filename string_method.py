# string method

course = "Python Programming"

print(course.upper())  # convert upper in a string
print(course.lower())  # convert lower
print(course.title())  # conver capital in first character of every word

name = "      My name is Tomal. I am student of Uttara university       "

print(name)
# remove whitespace from string both side begining or end of a string
print(name.strip())
print(name.lstrip())
print(name.rstrip())

print(name.find("Tomal"))  # find somethin from string
print(name.replace("Tomal", "Tom"))  # replace something from string

print("Tomal" in name)  # find somethin in a string and return boolean value
print("Tomal" not in name)


# numbers------

x = 10
x = 0b10
print(x) #print binaly value o x
print(bin(x)) # print binary representation

x = 0x12c
print(x) #print hexa for using 0x
print(hex(x)) #if print hex format then use this buildin function

#complex number a+ib
x = 1 + 2j
print(x)
