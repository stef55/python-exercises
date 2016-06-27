#print the result of a sum outside the function
def calculator(n1,n2):
    r=n1+n2
    return r
numbers={3:2,4:11,1:18}
for key,value in numbers.items():
    result=calculator(key,value)
    print(str(key)+'+'+str(value)+'='+ str(result))  
