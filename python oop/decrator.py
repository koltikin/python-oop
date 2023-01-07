def wapper_func(orijnal):
    def inner_fun(name, age, last):
        orijnal(name, age)
        print(f"this is you last_name {last}")
    return inner_fun


@wapper_func
def orijnal(age, name):
    print(f"my name is {name}")
    print(f"my age is {age}")


# after_dec = wapper_func(orijnal)

# after_dec(25, "ziya", "yilmaz")


orijnal(25, "ziya", "yilmaz")
