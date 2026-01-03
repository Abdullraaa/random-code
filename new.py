

name = input('name?: ')

if ' ' in name or len(name) < 5 or name[0].islower():
    print('invalid username')
else:
    print('username valid')