def outer():
    print("inside outer function")    

    def inner():
        print("inside inner function")

    return inner 



inner=outer()
inner()
inner()