def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function") 

outer()
inner()  #NameError