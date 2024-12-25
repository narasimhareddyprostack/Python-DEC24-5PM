def login_required(func):

    def inner(name,status):
        if status == False:
            print("Login Required")
        else:
            func(name,status)

    return inner


def home_page(name,login_st):
    print("Home Page")

def about_page(name,login_st):
    print("About")


@login_required
def history_page(name,login_st):
    print("History Page")
@login_required
def profile_page(name,login_st):
    print("Profile Page")

home_page("Rahul",True)
about_page("Rahul",False)
history_page("Rahul",False)
profile_page("Rahul",False)