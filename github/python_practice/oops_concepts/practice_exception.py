# print(10*1/0)
# print(4+spam*3)
# print("2"+2)
while True:
    try:
        x = int(input("please enter a number: "))
        break
    except ValueError:
        print("OOps! That was no valid Number . Try again...")
