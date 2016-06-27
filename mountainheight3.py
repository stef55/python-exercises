#print various information about the tallest mountains in the world
#creatae a function that convert meters in feet
def conversion(height):
    feet_height=height*3.28
    return feet_height
#dictionary with height of mountain and name
mountains = {'everest' : [8848], 'k2':[8611], 'kanchenjunga':[8586], 'lthose':[8516], 'makalu':[8463]}
#convert the values
for height in mountains.values():
    height.append(conversion(height[0]))
#print the names of teh mountains
print("mountain'sname")
print("\n")
for key in mountains.keys():    
    print("\n")
    print(key)
print("\n")
#print mountains height
print("mountain's heights in meter")
print("\n")
for value in mountains.values():
    print("\n")
    print(value[0])
print("\n")

print("mountain's heights in feet")
print("\n")
for value in mountains.values():
    print("\n")
    print(int(value[-1]))
#print sentences about the mountain

for name,height in mountains.items():
    print("\n")
    print(name+' '+'is '+str(height[0])+' meter tall,or '+str(int(height[-1]))+' feet')
