a=100
def outer():
    b=10
    a=20
    print("this is local : ", a)
    def inner():
        nonlocal b
        print("this is nonlocal : ",b)
    inner()
outer()
print("this is global : ",a)