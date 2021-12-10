def gen(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b
n=int(input("Vvesti s klaviaturu"))
t=gen(n)
for i in t:
    print(i)
