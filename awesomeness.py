"""create a list made by 5 name and add them to a list with wroten "is awesome"""
names=['Brian','Zac','Cody','Oronzo','randomname']
awesome_names=[name +' '+'is awesome' for name in names]
for awesome_name in awesome_names:
    print(awesome_name)
