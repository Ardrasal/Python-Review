# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# fruits2 = ('Apples')   # type will be string

# Single value needs trailing comma
fruits2 = ('Apples',)  # type will be tuple

# print(fruits2, type(fruits2))

print(fruits[1])

# fruits[0] = 'Pears'

# Delete tuple
del fruits2

print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add duplicate (can't have duplicates in sets)
fruits_set.add('Apples')

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

# Delete
# del fruits_set

print(fruits_set)
