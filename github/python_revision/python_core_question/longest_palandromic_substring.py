def longest_palindromic_substring(s):
    if not s:
        return ""

    n = len(s)
    start = end = 0

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(n):
        left1, right1 = expand_around_center(i, i)  # odd-length palindromes
        left2, right2 = expand_around_center(i, i + 1)  # even-length palindromes

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end+1]



if __name__ =='__main__':
    input_string = "rrrraavvii"
    result = longest_palindromic_substring(input_string)
    print(result)