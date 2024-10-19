# The motivation is:
# print("the result iS:" , (2*3+4))
# and the user will recieved : 10

def addition(a, b) :
    if a is None or b is None:
        return None
    return a+b

def subtraction(a, b) :
    if a is None or b is None:
        return None
    return a-b

def multiplication(a, b) :
    if a is None or b is None:
        return None
    return a*b

def division(a, b) :
    if a is None or b is None or b == 0:
        print("Cannot dividion on 0")
        return
    return a/b


def main() :
    a = 7
    b = 0
    act = "/"
    if act == "+":
        print(addition(a,b))
    elif act == "-":
        print(subtraction(a, b))
    elif act == "*":
        print(multiplication(a, b))
    elif act == "/":
        print(division(a, b))
    else:
        print("Noooo")

if __name__ == "__main__":
    main()
