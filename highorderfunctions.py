#High-order Functions
# like a wrapper? Wraps function in additoonal functonality runs before or after its called ?

numbers = [5, 7, 8, 9, 10,]

# #square nubmers funtion
# def squares(nums):
#     result = []
#     for i in nums:
#         result.append(i ** 2)
#     return result

# print(squares(nuumbers))   


#builds a new list with the result of e
# calling cb on each item in the list
def squares(nums, callback):
    result = []
    for i in nums:
        result.append(cb(n))
    return result

def square(n):
    return n * n

def  cube(n):
    return n ** 3

# print(squares(nuumbers)) 
# print(list(map(cube, numbers)))  #doing the same with built in map function - Cast to list so can view results
print(list(map(lambda x: x ** 2, numbers)))

evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))