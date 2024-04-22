def find_maximum_sum_subarray(arr):
    if not arr:
        return 0
    
    current_sum = arr[0]
    max_sum = arr[0]
    start = 0
    end = 0
    current_start = 0
    
    for i in range(1, len(arr)):
        if current_sum + arr[i] < arr[i]:
            current_sum = arr[i]
            current_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = current_start
            end = i
    
    return max_sum, arr[start:end+1]

if __name__=='__main__':
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, subarray = find_maximum_sum_subarray(array)
    print("Maximum sum:", max_sum)
    print("Subarray:", subarray)





