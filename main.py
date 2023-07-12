#Sum of odd numbers between 1-11
sum = 0

for num in range(1, 11):
    if(num % 2 != 0):
        sum +=num

print(sum)



#Sum of even numbers between 1-11
sum = 0
for num in range(1, 11):
    if(num % 2 == 0):
        sum+= num

print(sum)