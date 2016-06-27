#dictionary with height of mountain and name
mountains = {'everest' : '8848', 'k2':'8611', 'kanchenjunga':'8586', 'lthose':'8516', 'makalu':'8463',}
#print the names of teh mountains
print("mountain'sname")
print("\n")
for key in mountains.keys():    
    print("\n")
    print(key)
#print mountains height
print("mountain's heights")
print("\n")
for value in mountains.values():
    print("\n")
    print(value)
for name,height in mountains.items():
    print("\n")
    print(name+' '+'is '+height+' meter tall')
