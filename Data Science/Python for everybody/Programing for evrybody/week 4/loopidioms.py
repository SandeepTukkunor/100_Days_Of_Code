
#counting in loop

zork = 0
print("before", zork)

for i in [9, 41,13,3,74 , 15]:
    zork = zork +1
    print(zork, i )
print("After", zork)


#find total in the loop 
tot_sum = 0
print("sum is " , tot_sum)

for i in [9, 41,13,3,74 , 15]:
    tot_sum = tot_sum + i 
    print(tot_sum)

print("the sum of all digits  is" ,tot_sum)



#finding the averge in loop 

tot_sum = 0 
count = 0
for i in [9, 41,13,3,74 , 15]:
    count = count +1
    tot_sum = tot_sum + i 
    averge = tot_sum/ count
    

    print(count,averge,  tot_sum)

print("the average of list is:" ,tot_sum/count)

   





