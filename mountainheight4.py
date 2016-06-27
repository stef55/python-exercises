#print various information about the tallest mountains in the world
#dictionary in a dictionary
#dictionary with height of mountain and name
mountains = {'everest' : {'elevation':8848,'range':'himalaya'}, 'k2':{'elevation':8611,'range':'Karakora'}, 'kanchenjunga':{'elevation':8586,'range':'himalaya'}, 'lthose':{'elevation':8516,'range':'himalaya'}, 'makalu':{'elevation':8463,'range':'himalaya'}}
sorted(mountains)
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
    print(value['elevation'])
print("\n")
#print mountain's range
print("range of the mountain")
print("\n")
for value in mountains.values():
    print("\n")
    print(value['range'])
#print sentences about the mountain

for key,value in mountains.items():
    print("\n")
    print(key+' '+'is a'+str(value['elevation'])+' meter tall mountain in '+str(value['range'])+' range')
