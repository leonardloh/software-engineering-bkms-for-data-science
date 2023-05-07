# 1. Installation - PyLint, Flake8 and Black/AutoPEP8
# 2. Code Fixing
# 3. Autoformatter


import random

pi = 3.14

def CalcCircle             (rad,param="area"):
    if param=="area":
        return pi * rad ** 2
    elif param == "circumference":
        return 2 * pi * rad

def main()        :
    rad = 3
    # rad = random.randint(0, 5)

    print(f"Radius: {rad}")
    print(f"Calculated Area: {CalcCircle(rad=rad, param='area')}")
    print(f"Calculated Circumference: {CalcCircle(rad=rad, param='circumference')}")

    return

if __name__ == "__main__":
    main()