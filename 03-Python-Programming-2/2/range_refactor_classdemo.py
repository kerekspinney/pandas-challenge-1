numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print(f"Index: {i}, Value: {numbers[i]}")


numbers = [10, 20, 30, 40, 50]
for i, num in enumerate(numbers):
    print(f"Index: {i}, Value: {num}")

# example of for loop
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)


# list comprehension example
# [expression(element) for element in list (optional if filter)]
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)