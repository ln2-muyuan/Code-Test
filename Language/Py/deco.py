def deco(func):
    def wrapper(place):
        result = func(place)
        make_upper = result.upper()
        return make_upper
    return wrapper

@deco
def greeting(place):
    return "Welcome to " + place

print(greeting("New York"))

