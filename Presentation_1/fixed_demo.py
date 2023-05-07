"""
1. Installation - PyLint, Flake8 and Black/AutoPEP8
2. Code Fixing
3. Autoformatter
"""

import random

PI = 3.14


def calc_circle(rad, param="area"):
    """
    Calc Circle
    """
    if param == "area":
        return PI * rad ** 2

    if param == "circumference":
        return 2 * PI * rad

    return NotImplementedError


def main():
    """
    Main
    """
    # rad = 3
    rad = random.randint(0, 5)

    print(f"Radius: {rad}")
    print(f"Calculated Area: {calc_circle(rad=rad, param='area')}")
    print(
        f"Calculated Circumference: \
            {calc_circle(rad=rad, param='circumference')}"
    )


if __name__ == "__main__":
    main()
