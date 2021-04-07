courses = ['History', 'Maths', 'Physics', 'CompSci']
# print(courses.index('Maths'))
# for item in courses:
#     print(item)


''' getting both index and values '''
# for i, j in enumerate(courses, start=1):
#     print(i, j)


'''turn our list into strings'''

# course_string = '- '.join(courses)
# print(course_string)
#
#
# '''turn a string back into list'''
#
# new_list = course_string.split('-')
# print(new_list)



'''Tuples and sets   
tuples --- immutable , lists--mutable
Tuplese supports all other operation as list except append,remove and all other operations that are mutable'''

# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
# print(list_1)
# print(list_2)
#
# list_1[0] = 'Art'
#
# print(list_1)
# print(list_2)



# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
#
# print(tuple_1)
# print(tuple_2)
#
# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)



# '''Sets similiar to list and tuple, curly braces and no duplicates and unordered'''
#
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design' }
# print(cs_courses)
#
# '''sets are efficient in finding whether certain element lies within it or not'''
#
# print('Math' in cs_courses)
# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference((art_courses)))
# print(cs_courses.union(art_courses))



''''How to create empty list, tuple and sets '''


# empty list

empty_list = []
empty_list = list()


# empty tuples
empty_tuple = ()
empty_tuple = tuple()

# empty sets

empty_set = {} # this is wrong, this creates empty dictionary not empty set
empty_set = {}


