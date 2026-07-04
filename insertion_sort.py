# Insertion Sort Algorithm in monotonically decreasing order

numbers = [12, 4, 19, 7, 19, 2, 10]
# For loop Algorithm in monotonically decreasing order
for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    # Move smaller numbers to the right
    while j >= 0 and numbers[j] < key:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key
# Printing the result
print("Sorted list in decreasing order:", numbers)