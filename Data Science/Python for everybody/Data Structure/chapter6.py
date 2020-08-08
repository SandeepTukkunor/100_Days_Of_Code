

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

