# d = {x:i.count(x) for x in i}
def dict_count(a,b):
    dict_a={x:a.count(x) for x in a}
    print(dict_a)

    dict_b={c:b.count(c) for c in b}
    if dict_a==dict_b:
        return True
    return False

if __name__ =="__main__":
    print(dict_count("ravi","trvi"))