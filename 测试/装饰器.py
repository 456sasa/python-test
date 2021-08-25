# def my_decorator(func):
#     name = "Bob"
#     def wrapper(*args, **kwargs):
#         print("wrapper of my_decorator")
#         print(f"name is {name}")
#         func(*args, **kwargs)
    
#     return wrapper

# @my_decorator
# def greet(name,age,message):
#     print(f"my name is {name},{age} years old,{message}")

# greet("archer",18,'hello world')



def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print(f"--------{i}--------")
                print("wrapper of my_decorator")
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(message):
    print(message)
greet("hello world")