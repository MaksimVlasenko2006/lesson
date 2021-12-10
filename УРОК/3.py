a=["Python","Java","C","C++","C#"]
def gen(a):
    for i in a:
        yield(i)
t=gen(a)
for i in t:
    print(i)

    
