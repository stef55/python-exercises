#recreate a code without list comprehension
numbers=[]
for number in range (1,11):
    numbers.append(number)
numbers13=[]
for number in numbers:
    numbers13.append(number+13)
for number13 in numbers13:
    print(number13)
    
