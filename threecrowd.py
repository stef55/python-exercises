#different outputs based upon the number of elements in a list
def crowd_control (value1):
    if len(value1)>3:
        print("three is a company but two is none")

names=['Cody','james','Brian','lucy']
crowd_control (names)
del names[1]
del names[2]
crowd_control (names)



