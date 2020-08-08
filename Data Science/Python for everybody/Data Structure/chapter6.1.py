

#name = input("enter name:")

#print(name)


"""
apple = input("Enter:")
print(apple)
print(type(apple))
x =int(apple)- 10 # we cannot substract a string in int, so convert that string to int 
print(x)


"""

# accessing a charecter from the sting 
fruit = "Banana"
letter = fruit[2]
print(letter)


x = 3
w = fruit[x-2]
print(w)


print(len(fruit)) #lenght of a string



# looping through string
fruit = "banana"

index = 0

while index<len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index+1


# another easy method is use "for loop"
fruit = "banana"

for letter in fruit:
    print(letter)


# looping and counting 

word = "banana"
count = 0

for i in word:
    if i == "a":
        count = count+1

print(count)


#looking deeper into "in"

for letter in "banana":
    print(letter)



#slicing 
s = "Monty Python"

print(s[0:3]) #includes first but not upto, that means it will not count 3rd..
