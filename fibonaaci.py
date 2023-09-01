
# find the nth fibonacci number
n = int(input("Enter the nth fibbonacci number you want:\t"))


def fib(n):
    a = 0
    b = 1
    l = [1]
    for i in range(n+1):

        b = b+a

        a = l[i]
        l.append(b)
    print(l)
    return (l[n])


print(fib(n))
