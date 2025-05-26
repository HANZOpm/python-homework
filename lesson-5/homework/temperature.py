def convert_cel_to_far(C):
    F = C * 9 / 5 + 32
    return F
def convert_far_to_cel(F):
    C = (F - 32) * 5 / 9
    return C

C = input("Enter a temperature in degrees C: ")

try:
    C = float(C)
    F = round(convert_cel_to_far(float(C)), 2)
    print(f"{C} degrees C = {F} degrees F")
except:
    print("Please enter only numbers")

F = input("Enter a temperature in degrees F: ")

try:
    F = float(F)
    C = round(convert_far_to_cel(float(F)), 2)
    print(f"{F} degrees F = {C} degrees C")
except:
    print("Please enter only numbers")