x=''
y=2
if x and y:
    print('Both')
elif not (x or  y):
    print("Nothing")
elif not x or y:
    print('y')
elif  x or not y:
    print('x')
elif x and y:
    print('x,y')
