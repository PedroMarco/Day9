__author__ = 'acpb859'

try:

# open
    f = open('Info.txt', 'r')

# some operation
    a = 1/0
    f.close()

except ZeroDivisionError:
    print('There was a zero div err')
finally:
    f.close()
    if f.closed:
        print('the file is closed')
    else:
        print('file not closed')

