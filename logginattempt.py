def logging_attempts():
    attempts = ["admin:fail", "ra:pass", "audit:pass", "admin:fail"]
    fails = {}

    for entry in attempts:
        username, status = entry.split(":")

        if status == "fail":
            if username in fails:
                fails[username] += 1
            else:
                fails[username] = 1

    for user, count in fails.items():
        if count > 1:
            print(f"{user} faild to loggin {count} times!!!")



logging_attempts()
