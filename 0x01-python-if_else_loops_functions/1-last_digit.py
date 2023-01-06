#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = str(number)
num = int(st[len(st)-1])
if number < 0:
    print('Last digit of', st, 'is' ,-num ,'and is less than 6 and not 0')
elif num == 0:
    print('Last digit of', st, 'is' ,num ,'and is', num)
elif num > 5:
    print('Last digit of', st, 'is' ,num ,'and is greater than 5')
elif num <=5:
    print('Last digit of', st, 'is' ,num ,'and is less than 6 and not 0')
