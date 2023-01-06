#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = str(number)
num = int(st[len(st)-1])
if num == 0:
    print('Last digit of', st, 'is' ,num ,'and is', num)
if num > 5:
    print('Last digit of', st, 'is' ,num ,'and is greater than 5')
if num <=5:
    print('Last digit of', st, 'is' ,num ,'and is less than 6 and not 0')
