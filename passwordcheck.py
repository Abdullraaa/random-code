def password_check():

    password = input("enter a password: ")
    specal = "!@#$%&-"

    has_upper = False
    has_digit = False
    has_specal = False

    if len(password) < 8:
        print("weak password")
        print("less then 8 characters")
        return

    for char in password:
        if char.isupper:
            has_upper = True
        elif char.isdigit:
            has_digit = True
        elif char in specal:
            has_specal = True


    if has_upper and has_digit and has_specal:
        print("password is strong")
    else:
        print("weak password")
        if not has_specal:
            print("missing specal character")
        if not has_digit:
            print("missing digits")
        if not has_upper:
            print("missing uppercase letters")



password_check()

