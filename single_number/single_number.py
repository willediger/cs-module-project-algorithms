'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# using python base functionality
# def single_number(arr):
    # return [i for i in set(arr) if arr.count(i) == 1][0]

def single_number(arr):
    while True:
        num = arr.pop(0)
        try:
            arr.remove(num)
        except:
            return num


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")