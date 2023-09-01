
dig = int(input("Enter the number:\t"))


def sum(dig):
    s = 0
    t = 0
    while(dig > 0):

        n = dig % 10
        dig = dig//10
        if (n % 2 == 0):
            s = n+s
        else:
            t = n+t
    print("Sum of even digit and odd digit\t", s, t)


sum(dig)
