def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    lcs_matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_matrix[i][j] = lcs_matrix[i - 1][j - 1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i - 1][j], lcs_matrix[i][j - 1])

    lcs_length = lcs_matrix[m][n]
    lcs = [""] * lcs_length
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif lcs_matrix[i - 1][j] > lcs_matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


if __name__ =='__main__':
    str1 = "Ravi"
    str2 = "Ranjan"
    result = longest_common_subsequence(str1, str2)
    print(result)