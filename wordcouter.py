
def wordcounter():

    words = ["error", "login", "error", "fail", "login", "error"]
    lists = {}

    for unit in words:
    
        if unit in lists:
            lists[unit] += 1
        else:
            lists[unit] = 1

    for name, count in lists.items():
        print(f"{name}:{count}") 
    

wordcounter()


