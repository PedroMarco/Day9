__author__ = 'acpb859'
try:
    with open('Info.txt', 'r') as f:
        a = f.read()
        a = 1/0
except ZeroDivisionError:
    if f.closed:
        print('the file is closed')
    else:
        print('file not closed')