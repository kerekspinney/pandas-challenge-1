""" Anonymous Functions"""

def modulus2(number):
    if number % 2 == 0:
        return True
    else:
        return False




# 1. Get the even numbers from a list using the filter and lambda functions.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(modulus2, numbers))
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers2 = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers2)


even_numbers3 = []
for x in numbers: 
    if x % 2 == 0:
       even_numbers3.append(x) 
    else:
        pass
print(even_numbers3)



# 2. Use the map and lambda functions to add the numbers from both lists.
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(type(result))

for num in result:
    print(num)


print(result)

# 3. Use the map and lambda functions to split the following sentence into words.
sentence = "My favorite hobby is coding in Python"
words = list(map(lambda x: x.strip().title(), sentence.split()))
print(words)
