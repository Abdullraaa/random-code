
def usrname_scanner():
    usr_name = input("enter your username: ")


    has_upper = False
    has_digit = False
    has_space = False


    if len(usr_name) < 6:
        print("username is less than six characters")
        print("usename invalid")
        return
        

    for char in usr_name:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if char in " ":
            has_space = True


    if has_upper is True and has_digit and has_space is False:
        print("valid")
    else:
        print("invalid")


usrname_scanner()


#correct way to do it

def username_scanner():
    username = input("Enter your username: ")

    has_space = False

    if len(username) < 6:
        print("Username is INVALID")
        print("- Must be at least 6 characters long")
        return

    if not username[0].isalpha():
        print("Username is INVALID")
        print("- Must start with a letter")
        return

    for char in username:
        if char == " ":
            has_space = True
        elif not char.isalnum():
            print("Username is INVALID")
            print("- Must contain only letters and numbers")
            return

    if has_space:
        print("Username is INVALID")
        print("- Must not contain spaces")
        return

    print("Username is VALID")


username_scanner()

