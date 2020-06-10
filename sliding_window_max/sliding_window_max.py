'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    results = []

    window = nums[:k]
    curr_max = max(window)
    prev_num = window.pop(0)

    results.append(curr_max)
    for i in range(k,len(nums)):
        new_num = nums[i]
        window.append(new_num)
        if new_num > curr_max:
            curr_max = new_num
        elif prev_num == curr_max:
            curr_max = max(window)
        prev_num = window.pop(0)
        results.append(curr_max)
        i += 1
    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
