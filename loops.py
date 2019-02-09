# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sarah', 'Ardra']

# Simple for loop
# for person in people:
#     print(f'Current Person: {person}')

# Break out of a loop
# for person in people:
#     if person == 'Sarah':
#         break
#     print(f'Current Person: {person}')
# (The above stops before printing Sarah.)

# Continue
# for person in people:
#     if person == 'Sarah':
#         continue
#     print(f'Current Person: {person}')
# (The above skips Sarah.)

# range
# for i in range(len(people)):
#     print(people[i])
# (Prints all the people.)

# for i in range(0, 11):
#     print(f'Number: {i}')
# (Prints 0 to 10)

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1
# (Counts 0 to 10.)
