#list
numbers = [1, 2, 3, 4, 5]
names = ["Ali", "Sara", "John"]
mixed = [1, "Python", 3.5, True]

print(numbers)
print(names)
print(mixed)
# print in format
numbers = [1, 2, 3, 4, 5]
names = ["Ali", "Sara", "John"]
mixed = [1, "Python", 3.5, True]
print(*numbers, sep="\n")
print(*names, sep="\n")
print(*mixed, sep="\n")


print("List is always written in square brackets")
print("Its a list of items")
list1=['mango','watermelon','orange']
print(*list1, sep='\n')

#list with mixed data types

data = [1, "Python", 2.5, True]
print(data)
print(*data, sep='\n') # print in indexing form

# Nested List

matrix = [[1, 2], [3, 4]]
print(matrix)
print(*matrix, sep='\n')

# list of ranges
nums = list(range(1, 10)) #only 1 to 9 is  in result due to python reading 0 to 9 as 10 range?
print(nums)
print(*nums, sep='\n')

# comprehension

squares = [x * x for x in range(1, 5)  # explain this what its doing as result is coming 16
print(squares)
print(*squares, sep='\n')
















