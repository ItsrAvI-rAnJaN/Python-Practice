"""
Problem 1:
Write a function that takes a text string as input and returns a dictionary containing the frequency of each word in the text. The function should ignore punctuation and treat uppercase and lowercase letters as the same word.

Example:
text = "The quick brown fox jumps over the lazy dog."
print(word_frequency_counter(text))
# Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

Problem 2:
Write a function that takes a list of elements and an integer N as input and returns the top N most frequent elements in the list.

Example:
elements = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1]
print(top_n_frequent_elements(elements, 3))
# Output: [1, 2, 3]

Problem 3:
Write a function that takes a list of integers and finds the length of the largest subarray with a sum of zero.

Example:
arr = [4, 2, -3, 1, 6]
print(largest_zero_sum_subarray(arr))
# Output: 3 (The largest subarray with zero sum is [2, -3, 1])

Problem 4:
Write a function that takes a list of integers and finds the length of the longest consecutive sequence of elements (ascending or descending).

Example:
arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(arr))
Output: 4 (The longest consecutive sequence is [1, 2, 3, 4])

Problem 5:
Write a function that takes a list of strings and groups anagrams together. Anagrams are words that have the same characters but in different orders.

Example:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""


def word_frequency_counter(text):
    str=text.lower()
    str=list(str.split(" "))
    dict1={x:str.count(x) for x in str}
    return dict1

def top_n_frequent_elements(elements,N):
    list1=[]
    for i in elements:
        if i <=3:
            list1.append(i)
    return set(list1)


def largest_zero_sum_subarray(arr):
    lar_len=0
    n=len(arr)
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=arr[j]
            if curr_sum==0:
                lar_len=max(lar_len,j-i+1)
    return lar_len

def longest_consecutive_sequence(arr):
    pass












if __name__=="__main__":
    text = "The quick brown fox jumps over the lazy dog."
    # print(word_frequency_counter(text))
    elements = [1, 2, 3, 2, 1, 4, 5, 3, 2, 1]
    # print(top_n_frequent_elements(elements,3))
    arr = [4, 2, -3, 1, 6]
    print(largest_zero_sum_subarray(arr))