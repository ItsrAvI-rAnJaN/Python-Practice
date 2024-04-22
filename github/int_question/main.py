"""
aeroplane: unique alphalet
"""

def find_unique(str):
    n=len(str)
    list1=[]
    for i in range(0,n):
        if str.count(str[i]) != 1:
            list1.append(str[i])

    return list1



if __name__ =="__main__":
    print(find_unique("aeroplane"))