while True:
    try:
        a, b, c = map(int, input().split(' '))
        if a == b and b == c:
            print("*")
        elif a == b:
            print("C")
        elif a == c:
            print("B")
        else:
            print("A")
    except EOFError:
        break