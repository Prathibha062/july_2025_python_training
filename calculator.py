try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    action = input("Enter the action (add, sub, mul, div): ")
    
    if action == "add":
        res = n1 + n2
        print(res)
    elif action == "sub":
        res = n1 - n2
        print(res)
    elif action == "mul":
        res = n1 * n2
        print(res)
    elif action == "div":
        res = n1 / n2
        print(res)
    else:
        raise ValueError("Invalid operation")
except ValueError as e:
    print("ValueError:", e)

