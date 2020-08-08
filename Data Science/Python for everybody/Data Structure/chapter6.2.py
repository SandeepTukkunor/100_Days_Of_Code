# manupulating strings 
a = "hello"
b = a + " there"

print(b)

"""
#variable in can also be used as logial operator 
fruit = "banana"
"n" in fruit
#this has to be done in cdmd

"""

# string library
greet = "GOOD MORNING"
greet1 = greet.lower()
print(greet1)

greet = greet1.upper()
print(greet)


# what strings are capable of 
stuff = "hello world"
print(type(stuff))

print(dir(stuff))

#searching in string 
fruit = "banana"

pos = fruit.find("na") #where is the position of banana
print(pos)


# serach and replaec

greet = "hello bob"
print(greet.replace("bob", "sandeep"))

#strip is used to earse the white space
greet = "   good morning   "
print(greet.rstrip())
print(greet.lstrip())
print(greet.strip())


print(len('banana')*7)


#exercise solution 
text = "X-DSPAM-Confidence:    0.8475";

iops = text.split(":")
print(iops[1])
sliced = iops[1].strip()


print(sliced)



