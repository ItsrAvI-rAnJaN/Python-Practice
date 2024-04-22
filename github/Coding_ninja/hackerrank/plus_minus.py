    # Write your code here
def plus_minus(arr):
    n=len(arr)
    neg=0
    pos=0
    zero=0
    for i in range(n):
        if arr[i]>0:
            pos+=1
        elif arr[i]==0:
            zero+=1
        else:
            neg+=1
    x=pos/n
    y=neg/n
    z=zero/n
    print("{:.6f}".format(x))
    print("{:.6f}".format(y))
    print("{:.6f}".format(z))
    
        

if __name__ == '__main__':
    arr=[-23,34,0,-2,5]
    plus_minus(arr)