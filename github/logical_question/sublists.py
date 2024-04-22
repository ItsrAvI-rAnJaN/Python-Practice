'''
Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]

advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
Notes
The sublists should be returned in the order of each element's first appearance in the given list.

'''

def advanced_sort(lst):
    dict_res = {}
    for i in lst:
        if i in dict_res:
            dict_res[i].append(i)
        else:
            dict_res[i] = [i]
    res = []
    for i in lst:
        if i in dict_res:
            res.append(dict_res[i])
            del dict_res[i]
    return res


if __name__ =="__main__":
    # arr=[2, 1, 2, 1]
    # arr=[5, 4, 5, 5, 4, 3]
    arr=["b", "a", "b", "a", "c"]
    print(advanced_sort(arr))         