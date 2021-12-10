list_int=[4,16,64,256]
list_gen=(i**1/2 for i in list_int)
print(next(list_gen))
while list_gen:
    print(next(list_gen))
