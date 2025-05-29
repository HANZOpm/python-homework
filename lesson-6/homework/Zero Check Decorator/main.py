def check(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except:
            result = "Denominator can't be zero"
        return result
    return wrapper
@check
def div(a, b):
    return a / b

print(div(6, 2))
print(div(6, 0))