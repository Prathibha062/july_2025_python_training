num=input("enter a number:")
try:
    if not num.isnumeric():
        raise ValueError("input is not a valid number")
    else:
        print(num)
except ValueError as e:
    print(e)