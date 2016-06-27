#multiple if in a function
def crowd_control (value1):
    if len(value1)>5:
        print("there is a mob")
    elif len(value1)<=5 and len(value1)>=3:
        print("there is a crowd")
    elif len(value1)==2 or len(value1)==1:
        print("it's not that crowdy")
    else:
        print("empty room")

names=['Cody','james','Brian','lucy']
crowd_control (names)
del names[1]
del names[2]
crowd_control (names)
