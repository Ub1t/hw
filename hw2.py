import math
x = float(input("Введите x: "))
PI = math.pi
if -PI <= x <= PI:
    print("y =", math.sin(3 * x))
elif -PI > x > PI:
    print("y =", x)
   
