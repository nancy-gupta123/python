
def cube(num):
    return num**3

#OR

cube =lambda x:x**3

print(cube(3))

#args
def sum_all(*args):
    print(args)
    for i in args:
        print(i*2)
    return sum(args)
print(sum_all(1,2,3,4))

#kwargs
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="Priyanka",profession="Engineer")
print_kwargs(name="Priyanka")
print_kwargs(name="Priyanka",profession="Engineer", domain="Software Developer")

#yield
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even_generator(10):
    print(num)



    #closure
    print("closure")
    def num(num):
        def g(x):
            return num**x
        return g
    
    f=num(3)
    g=num(2)

    print(g)
    print(f)
    
      