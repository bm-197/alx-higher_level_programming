#!/use/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = 0
for i in str(number):
    last_digit = int(i)
if last_digit > 6:
    print(f'Last digit of {number} is {last_digit} and is greater than 6')
elif last_digit == 0:
    print(f'Last digit of {number} is {last_digit} and is 0')
else:
    print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
