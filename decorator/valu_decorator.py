def discount_decorator(func):
    def wrapper(price):
        func(price)
        return func(price/2)
    return wrapper


@discount_decorator#without this it shows 100
def total(price):
    return price

print(total(100))