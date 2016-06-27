#check negative numbers and count them
numbers=[1,2,-1,-8,-7,15,22,23,167]
#number of negative numbers
nega=0
#number of positive numbers
pos=0
for number in numbers:
    if number<0:
        n=n+1
    else:
        p=p+1
print("there are %d negative numbers" %n)
print("there are %d positive numbers" %p)
