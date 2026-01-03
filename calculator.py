def run_cal():
    while True:
        a = float(input("pick a number: "))
        b = float(input("pick another number: "))
        
        op = input("pick an operation (+,-,*,/); ")
        
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        else:
            result = a / b
            
        print(result)
            
run_cal()