def minMinMax(numbers):
    """minMinMax machine.

    Given an unsorted array of integers, find the smallest number in the array, the largest number in the array, and the smallest number between the two array bounds that are not in the array.
    """

    smallest = min(numbers)
    minimumAbsent = smallest
    while (minimumAbsent) == min(numbers):
        numbers.remove(minimumAbsent)
        minimumAbsent += 1
    largest = max(numbers)
    
    return f'Smallest: {smallest} Minimum absent: {minimumAbsent} Largest: {largest}'

if __name__ == "__main__":
    print(minMinMax([1, 3, -3, -2, 8, -1]))