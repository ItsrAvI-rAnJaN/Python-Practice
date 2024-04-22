def count_print(a,b):
    dict_a=[]
    dict_b=[]
    list_a={}
    list_b={}
    for i in range(len(a)):
        dict_a.append(a[i])
    for k in range(len(dict_a)):
        count_val=dict_a.count(a[k])
        print(count_val)
        list_a.update(dict_a[k],count_val)


    for j in range(len(b)):
        dict_b.append(b[j])
    for n in range (len(dict_b)):
        count_b=dict_b.count(b[n])




if __name__ =="__main__":
    a="raviranjan"
    b="raivrajnan"
    print(count_print(a,b))



    