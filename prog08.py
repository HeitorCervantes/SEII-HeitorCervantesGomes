def find_index(to_search, target):
	for i, value in enumerate(to_search):
		if value == target
			return 1

	return -1

courses = ['History', 'Math', 'Physics']

index = find_index(courses, 'Math')
print(index)

#$ import name_modulo as another_name

#$ index = another_name.find_index(course, 'Math')

#$ from name_modulo import find.index as another_name_of_function

#$ index = another_name_of_function(course, 'Math')

import sys

print(sys.path)


import random

random_course = random.choice(courses)
print(random_course)

import math

rads = math.radians(90)
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

import os
print(os.getcwd())
print(os.__file__)

import antigravity
