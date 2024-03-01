#import math
from math import sqrt

number = 9
answer = sqrt(number)
print(answer)
print(f"the square root is {answer}")
print("the square root is", answer)

# the square root is 3

from random import randint, choice

random_number = randint(1, 10)
print(random_number)

fav_candy = ["twix", "twizzlers", "skittles", "gummy bears", "reeses"]
random_candy = choice(fav_candy)
print(f"today i'll eat {random_candy}")


from datetime import datetime, date

current_datetime = datetime.now()
print(current_datetime)

current_time = current_datetime.strftime("%H:%M:%S")
print(current_time)

current_time = current_datetime.strftime("%M:%S")
print(current_time)

current_date = date.today()
print(current_date)