def calculate(a,operator,b):
    if operator =="+":
        return a+b
    elif operator =="-":
        return a-b
    elif operator =="*":
        return a*b
    elif operator =="/":
        return a/b
    else:
        pass
a=int(input("1st value"))
b=int(input("2nd value"))
operator=input("enter operator:+,-,*,/")
print(calculate(a,operator,b))