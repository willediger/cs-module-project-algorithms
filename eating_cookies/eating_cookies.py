'''
Input: an integer
Returns: an integer
'''
#naive solution
# def eating_cookies(n):
#     if n <= 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

def eating_cookies(n, memo=[]):
    memo.extend([0]*(n-len(memo)+1))
    def eating_cookies_memoized(n):
        if memo[n]:
            return memo[n]
        if n <= 1:
            memo[n] = 1
        elif n == 2:
            memo[n] = 2
        else:
            memo[n] = eating_cookies_memoized(n-3) + eating_cookies_memoized(n-2) + eating_cookies_memoized(n-1)
        return memo[n]
    eating_cookies_memoized(n)
    return memo[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
