# TODO: Evaluate the put of global variable memo to
#  do memoization with several call

def countWays(n, memo=None):
    if not memo:
        memo = [-1 for i in range(n+1)]
        return countWays(n, memo)
    else:
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif memo[n] > -1:
            return memo[n]
        else:
            memo[n] =   countWays(n-1, memo) + \
                        countWays(n-2, memo) + \
                        countWays(n-3, memo)
            print(n, memo)
            return memo[n]

if __name__ == "__main__":
    print(countWays(9))