
def authsystem():
    usrname = input("enter your username: ")
    passwrd = input("enter your passwrd: ")
    specail = "!@#$%^&*()"

    usr_has_space = False
    pass_has_space = False
    pass_has_specail = False
    pass_has_upper = False
    pass_has_digit = False

    if len(usrname) < 6:
        print("username is less than six characters")
        print("try again")
        return

    if not usrname[0] .isalpha():
        print("invalid username")
        print("first character must be a letter")
        return

    for char in usrname:
        if char == " ":
            usr_has_space = True
            print("invalid username")
            print("username has space")
            return

        elif not char .isdigit() and not char .isalpha() and not char .isupper():
            print("invalid username")
            print("username name must contain at least Uppercase, number and, letters")
            return

    if len(passwrd) < 8:
        print("invalid password")
        print("password must be at least 8 characters")
        return

    for char in passwrd:

        if char .isupper():
            pass_has_upper = True

        if char .isdigit():
            pass_has_digit = True
 
        if char in specail:
            pass_has_specail = True

    if pass_has_digit and pass_has_upper and pass_has_specail:
        print("access granted")

    else:
        print("weak logins")

        if not pass_has_digit:
            print("password lacks number")
            print("--------------------")
        if not pass_has_specail:
            print("password lacks specail character")
            print("--------------------")
        if pass_has_space:
            print("password has space")
            print("--------------------")
        if not pass_has_upper:
            print("password lacks Uppercase")
            print("--------------------")


authsystem()
