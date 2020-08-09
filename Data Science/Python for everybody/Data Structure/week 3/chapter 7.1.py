# first we have to open a file
#fhand = open("mbox-short.txt", ) # making file available for python 
#print(fhand)


stuff = "hello \nworld"
print(stuff)

"""
file = open("mbox-short.txt")
for cheese in file:
    print(cheese)

    # prints all the lines from text 
"""


file = open("mbox-short.txt")
for line in file:
    line = line.strip()  # removes the space which the following line creates 
    if line.startswith("From:"):
        print(line)


# skippinf with continue
file = open("mbox-short.txt")
for line in file:
    line = line.strip()
    if not line.startswith("From:"):
        continue
    print(line)



#using "in" to select lines 
file = open("mbox-short.txt")
for line in file:
    line = line.strip()
    if not "@uct.ac.za" in line:
        continue
    print(line)


#dealing with bad names 
file = input("please enter ur file name: ")

try:
    fileopen = open(file)
except:
    print("please enter a valid file name and check for the directory in case you have lost", file)

count = 0

for line in fileopen:
    if line.startswith("Subject:"):
        count = count+1
print("there were ", count, "subject lines ", file)
    


