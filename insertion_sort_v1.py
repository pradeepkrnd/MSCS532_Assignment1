# Insertion Sort Algorithm in monotonically decreasing order
def insertion_sort_decreasing(numbers):
    for j in range(1, len(numbers)):
        key = numbers[j]
        i = j - 1

        # Shift smaller values to the right.
        while i >= 0 and numbers[i] < key:
            numbers[i + 1] = numbers[i]
            i -= 1

        # Insert the key in its correct descending position.
        numbers[i + 1] = key

    return numbers
# A sample data is here
numbers = [10, 4, 25, 8, 2, 15]
print(insertion_sort_decreasing(numbers))