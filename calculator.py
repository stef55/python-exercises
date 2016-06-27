#function that add two numbers and printe both them and the result
def calculator(n1,n2):
    r=n1+n2
    print(str(n1)+'+'+str(n2)+'='+str(r))
numbers={4:3,2:1,12:1}
for key,value in numbers.items():
    calculator(key,value)
