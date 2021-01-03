def apple_orange(s, t, a, b, apples, oranges):

    # print(s)
    # print(t)
    # print(a)
    # print(b)
    # print(apples)
    # print(oranges)

    for apple in apples:
        print(apple)

    print("a",a)
    app = [a+apple for apple in apples if (a+apple)>=s and (a+apple)<=t]
    orr = [b+orange for orange in oranges if (b+orange)>=s and (b+orange)<=t]

    print(app,orr )
    print(len(app))
    print(len(orr))

if __name__ == "__main__":
    s=7
    t=11
    a=5
    b=15
    apples = [-2, 2, 1]
    oranges = [5, -6]
    print("hello")
    apple_orange(s, t, a, b, apples, oranges)
