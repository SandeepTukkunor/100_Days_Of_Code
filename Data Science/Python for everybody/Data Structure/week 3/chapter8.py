lis = [1,2,3,4,5]
for i in lis:
    print(i)

print("Blastoff")

#strings are immutable and lists are mutable
lotto = [1,5,6,3,4,8]
# if we want to change 5 to 9
lotto[1] = 9
print(lotto)



#range function 
print(list(range(5)))

friends = ["Sandeep" , "sunil", "Anil"]
print(len(friends))
print(list(range(len(friends))))




# Manupulating lists 
friends = ["Sandeep" , "sunil", "Anil"]
for friend in friends:
    print("Happy new year", friend)


# slicing works siilar to string 
#concnatenating also work similar to strings


#building a list from scratch 

stuff = list()
stuff.append("book")
stuff.append(99)
stuff.append("cookie")
print(stuff)


#is somthing in the list
some = [1,3,4,2,6,7,3,4,6]
print(9 in some)

print(min(some)) #to find the minimum
print(max(some))

"""
total = 0 
count = 0 

while True:
    inp = input("please enter a number")
    if inp == "done":
        break
    Value = float(inp)
    total = total + Value
    count = count+1
print("Average", total/count)
"""
"""
numlist = list()
while True:
    inp = input("please enete a number")
    if inp == "Done":
        break
    value = float(inp)
    numlist.append(value)
print("The average is", sum(numlist)/ len(numlist))
# this method uses lists

"""

#Best friends , strings and lists 

word = "hello there how are you"
stuff = word.split()
print(stuff)
# the string will be converted to list
print(len(stuff))



# reading   and splitting file with the help of list and array
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    words = line.split()
    print(words)


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(len(c))