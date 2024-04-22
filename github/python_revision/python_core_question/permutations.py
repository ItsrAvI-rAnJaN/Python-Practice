def permute_string(string):
    if len(string) == 0:
        return ['']
    prev_list = permute_string(string[1:len(string)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(string)):
            new_str = prev_list[i][0:j]+string[0]+prev_list[i][j:len(string)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list



if __name__ =='__main__':
    print(permute_string("ravi"))