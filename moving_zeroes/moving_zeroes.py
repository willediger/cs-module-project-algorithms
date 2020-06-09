'''
Input: a List of integers
Returns: a List of integers
'''

def moving_zeroes(arr):
    # Your code here
    zero_count = 0
    i = 0
    while i < len(arr) - zero_count:
        if arr[i] == 0:
            j = len(arr) - 1 - zero_count
            while arr[j] == 0 and j > i:
                j -= 1
            arr[i] = arr[j]
            arr[j] = 0
            zero_count += 1
        i += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")