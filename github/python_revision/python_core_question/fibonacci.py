def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
   for i in range(n):
        print(recur_fibo(i))



if __name__=='__main__':
    result=recur_fibo(10)
    print("Fibonacci sequence:",)
    