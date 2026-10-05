# string is a sequence of unicode character that handle the text. string are enclosed in single quotel, double  quote and triple code which are use for multiline text. Pythone string are immutable

name = "Tomal khan"  # initialize
about_me = """My name is Tomal. \nI am learning Python programming."""  # Multiline sring


print(name)
print(about_me)

print(len(about_me))  # print the lenth of a string

# concatination
full_name = name + " Munna"
print(full_name)

# Repetation
print(name * 3)


print("Tomal" in about_me)  # Returns True if substring exists, else False

# Accessing Characters
print(about_me[0]) #print the zero index
print(about_me[-1]) #print last characeter
print(about_me[0:3]) #from 0 index to total three lenth
print(about_me[4:]) #from 4 to end
print(about_me[:2])
print(about_me[:])


# f-string
age = 24
print(f"My name is {name}. My age is {age}")


# Built-in String Methods
capital_name = name.upper()
print(capital_name)

small_name = name.lower()
print(small_name)

text = "            remove whitespace from left and right from a string use strip() function     "
print(text.strip())

print(name.replace("khan", "Hossain"))#replace string