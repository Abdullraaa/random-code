
def log():

    logs = [
    "admin:192.168.1.10:fail",
    "admin:192.168.1.10:fail",
    "ra:10.0.0.5:pass",
    "admin:10.0.0.5:fail",
    "ra:10.0.0.5:fail"
]

    dic = {}

    for entery in logs:
        usrname, ip, status = entery.split(":")

        if status == "fail":
            if usrname not in dic:
                dic[usrname] = {}
            if ip not in dic[usrname]:
                dic[usrname][ip] = 1
            else:
                dic[usrname][ip] += 1

    for name, ips in dic.items():
        for ip, count in ips.items():
            print(f"{name} from {ip} failed {count} times")
log()