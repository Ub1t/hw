import math
x = float(input("Введите x: "))
PI = math.pi
if -PI <= x <= PI:
    print("y =", math.cos(3 * x))
elif -PI > x > PI:
    print("y =", x)
   
