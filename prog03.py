courses = ['history', 'math', 'physics']

print(courses[0])
print(courses[1])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[1:])

courses.append('Art')
print(courses)

courses.insert(0, 'CompSci')
print(courses)

courses2 = ['Education', 'Portuguese']
courses.insert(0, courses2)
print(courses)

print(courses[0])

courses3 = ['Anatomy', 'Physiology']
courses.extend(courses3)
print(courses)

sorted_courses = sorted(courses)

courses.remove('Math')
print(courses)

popped = courses.pop()
print(popped)

courses.reverse()
print(courses)

courses.sort()
nums = [1,5,8,2,10,50,38]
nums.sort()
print(courses)
print(nums)

courses.sort(reverse=True)
nums = [1,5,8,2,10,50,38]
nums.sort(reverse=True)
print(courses)
print(nums)

print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))

print('Art' in courses)

for each in courses: print(each)

for index, each in enumerate(courses, start=1): print(index, each)

course_str = ', '.join(courses)
print(course_str)

list = course_str.split(', ')
print(list)

list1 = ['history', 'math', 'physics']
list2 = list1
print(list1)
print(list2)

list1[0] = 'Art'
print(list1)
print(list2)

cs_course = {'history', 'math', 'physics'}
print(cs_course)

art_course = {'history', 'math', 'Art'}
print(cs_course.intersection(art_course))
print(cs_course.difference(art_course))
print(cs_course.union(art_course))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = set()

