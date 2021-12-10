def gen(n):
    print("первый перебор")
    yield n
    print("sekond")
    yield n+1
    print("third") 
    yield n*3
n=int(input("Введите число"))
t=gen(n)
for i in t:
    print(i)
