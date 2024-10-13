def min_deletion_insertion(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                deletion = dp[i - 1][j] + 1
                insertion = dp[i][j - 1] + 1
                substitution = dp[i - 1][j - 1] + 1
                dp[i][j] = min(deletion, insertion, substitution)

    deletion_count = 0
    insertion_count = 0
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            deletion_count += 1
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            insertion_count += 1
            j -= 1
        else:
            i -= 1
            j -= 1

    return deletion_count, insertion_count

str1 = "heap"
str2 = "pea"
deletion_count, insertion_count = min_deletion_insertion(str1, str2)

print("Minimum Deletion =", deletion_count)
print("Minimum Insertion =", insertion_count)