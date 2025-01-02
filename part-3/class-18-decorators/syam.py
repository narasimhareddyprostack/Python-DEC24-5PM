def outer():
    print("outer function")
    def inner():
        print("inner function")
    
    inner()
    inner()
    inner()



outer()

outer()