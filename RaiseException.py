def getArea(radius):
    if radius < 0:
        raise RuntimeError("Negative radius")
    
    return radius * radius * 3.1415

try:
    print(getArea(5))
    print(getArea(-5)) # This second value is wrong
except RuntimeError:
    print("Invalid radius")
