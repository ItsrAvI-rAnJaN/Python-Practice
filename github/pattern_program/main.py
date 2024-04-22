def star_pattern_1(n):
    for i in range(n+1):
        for j in range(i+1):
            print("*",end=" ")
        print("")

def star_pattern_2(n):
    k=1
    for i in range(n):
        for j in range(k):
            print("*",end=" ")
        k+=2
        print("")


def star_pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i+1):
            print("*",end=" ")
        print()

def reverse_pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end="")
        for k in range(1,n-i):
            print("*",end=" ")
        print()


def diamond_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i+1):
            print("*",end=" ")
        print()
    for i in range(n):
        for j in range(i+1):
            print(" ",end="")
        for k in range(1,n-i):
            print("*",end=" ")
        print()


if __name__=="__main__":
    # star_pattern_1(5)
    # star_pattern_2(5)
    # star_pyramid(5)
    # reverse_pyramid(5)
    diamond_pattern(5)