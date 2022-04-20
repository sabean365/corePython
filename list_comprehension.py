import random
hundred_num = [random.randint(18,100) for num in range(100)]
print("Random number list: " + str(hundred_num))

import math
even_nums = [math.log(num) for num in hundred_num if num%2==0]
print(even_nums)

import datetime
birth_year = [datetime.datetime.now().year - age for age in hundred_num]
print(birth_year)

import os
python_files = [f[:-3] for f in os.listdir() if f.endswith(".py")]
print(python_files)