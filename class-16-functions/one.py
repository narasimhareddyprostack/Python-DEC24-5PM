def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function") 
    inner()
    inner()

outer()