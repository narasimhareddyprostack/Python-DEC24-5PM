def login_req(func):

    def inner(name,status):
        if status==False:
            print("Login Required")
        else:
            func(name,status)

    return inner

@login_req
def profile_page(name,status):
    print("Profile Page")

profile_page("Rahul",False)