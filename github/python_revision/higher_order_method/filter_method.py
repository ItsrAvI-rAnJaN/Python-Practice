# from itertools import filterfalse
# num1=["red","rain","region",'blue','purple','green']

# result=filterfalse(lambda x:x.startswith("r"),num1)
# # print (result)#Output:<itertools.filterfalse object at 0x0148E4D8>

# # print (list(result))  

# from functools import reduce
# num1=[1,2,3,4,5]
# num2=reduce(lambda x,y:x+y,num1)
# num3=sum(num1)
# print (num2)#Output:120
# print(num3)

# from itertools import accumulate
# num1=[1,2,3,4,5]
# num2=accumulate(iterable)(num1,lambda x,y:x*y,)
# print (num2)
# #Output:<itertools.accumulate object at 0x02FE35C8>
# print (list(num2))



numbers = ('1', '2', '3', '4')
result = map(int,numbers)
print(list(result))