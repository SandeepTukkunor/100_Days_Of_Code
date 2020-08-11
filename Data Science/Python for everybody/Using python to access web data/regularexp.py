# extracting data 
import re
x = " my 2 favourite numbers are 17 and 18"
y = re.findall("[0-9]+", x)
print(y)



# greedy matching 
x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)


#non greedy 
x = "From: Using the : character"
y = re.findall("^F.+?:", x)
print(y)


x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y= re.findall("\S+@\S+", x)
print(y)


x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("@[^ ]*", x)
print(y)


filename = "actual_data.txt"
f = open(filename)
d = f.read()
y = re.findall('[0-9]+', d)
sum = 0
for i in range(len(y)):
    c = int(y[i])
    sum += c

print(sum)
