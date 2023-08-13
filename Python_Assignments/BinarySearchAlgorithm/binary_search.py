'''
In this example, the user is prompted to enter a sorted list of numbers, 
separated by spaces. They are also asked to enter the number they want to search for. 
The input is then converted into a list of integers. 
The binary_search function is called with the list and the target number as arguments.
 The result of the binary search is stored in the variable result.
  Finally, the program displays whether the target number was found or not, along with its index if found.

'''
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

    return -1

# Input from user
numbers = input("Enter a sorted list of numbers, separated by spaces: ")
target = int(input("Enter the number you want to search for: "))

# Convert input to list of integers
numbers = list(map(int, numbers.split()))

# Perform binary search
result = binary_search(numbers, target)

# Display result
if result != -1:
    print("Target found at index: ", result)
else:
    print("Target not found.")