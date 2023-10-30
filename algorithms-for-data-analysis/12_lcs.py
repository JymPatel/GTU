from pprint import pprint

def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    tracker = [[None] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                tracker[i][j] = "cross"
            elif dp[i - 1][j] > dp[i][j - 1]:
                dp[i][j] = dp[i - 1][j]
                tracker[i][j] = "up"
            elif dp[i - 1][j] <= dp[i][j - 1]:
                dp[i][j] = dp[i][j - 1]
                tracker[i][j] = "left"
            # else:
            #     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    pprint(dp)

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if tracker[i][j] == "cross":
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif tracker[i][j] == "up":
            i -= 1
        else:
            j -= 1

        # if str1[i - 1] == str2[j - 1]:
        #     lcs.append(str1[i - 1])
        #     i -= 1
        #     j -= 1
        # elif dp[i - 1][j] > dp[i][j - 1]:
        #     i -= 1
        # else:
        #     j -= 1
    
    return ''.join(reversed(lcs))

# Example usage
str1 = "AGGTAB"
str2 = "GXTXAYB"
result = longest_common_subsequence(str1, str2)
print("Longest Common Subsequence:", result)
