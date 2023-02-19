# function based decrator__________________


# def decrator(decrated_function):
#     def wrapper_fun(*args):
#         print(f"decrator excut this befor {decrated_function.__name__}")
#         decrated_function(args[0], args[1])
#         print(args[2])
#         print("after decrated_fun")

#     return wrapper_fun


# @decrator
# def decrated_function(name, age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")


# decrated_function("ziya", 32, "ziya kasgari")

# class based decrator__________________


class decrator:
    def __init__(self, b):
        self.b = b

    def __call__(self, *args, **kwargs):
        print("hello ziay")

        class new_b(self.b):
            def __init__(self, fname, lname, age):
                super().__init__(fname, lname)
                self.age = age

            def see_togather(self):
                print(
                    f"my full name is {self.first_name}{self.last_name}, my age is {self.age}"
                )

        return new_b(args[0], args[1], args[2])


@decrator
class decrated_function:
    def __init__(self, fname, lname):
        print(f"my name is {fname}")
        # print(f"my age is {age}")
        self.first_name = fname
        self.last_name = lname
        # self.age = age

    def see_togather(self):
        print(f"my full name is {self.first_name}{self.last_name}")


pp = decrated_function("ziya", "kasgari", 32)
pp.see_togather()
# pp.see_togather()

# decrate class with function __________________


# def decrator(fun):
#     def wraper(*args, **kwargs):
#         print(f"decrator excut thi befor {fun.__name__}")
#         print("after decrated_fun")
#         gg = fun(*args, **kwargs)
#         return gg

#     return wraper


# @decrator
# class decrated_function:
#     def __init__(self, name, age):
#         print(f"my name is {name}")
#         print(f"my age is {age}")
#         self.name = name
#         self.age = age

#     def see_togather(self):
#         print(f"my name is {self.name}, my age is {self.age}")


# # pp = decrated_function("ziya", 32)
# # pp.see_togather()


# # decrate function with class __________________


# class decrator:
#     def __init__(self, fun):
#         pass
#         # self.fun = fun
#         # print(f"decrator excut thi befor {self.fun.__name__}")
#         # print("after decrated_fun")

#     def __call__(self, *args, **kwds):
#         print("hello")
#         self.fun(*args, **kwds)
#         print("after hello")


# @decrator
# def decrated_function(name, age):
#     print(f"my name is {name}")
#     print(f"my age is {age}")
#     print(6 + 8)
#     print(f"my name is {name}, my age is {age}")


# # decrated_function("ziya", 32)
