import math

def main():
    "param-eq.ewb"
    R10 = 3000
    R11 = 3000
    R12 = 100000 # VR from 0 to 100 kOhm
    C4 = to_farads(1, "nF")
    C5 = to_farads(1, "uF")
    F = 1 /(2 * math.pi * math.sqrt( (R10 + R12) * C4 * (R11 + R12) * C5 ))
    print("F: {}".format(int(F)))

def to_farads(value: float, units: str):
    """
    :param value: value in units
    :param units: F, uF, mkF
    :return:
    """
    multiplier = {
        "": 1,
        "F": 1,
        "uF": (10 ** -6),
        "nF": (10 ** -9),
        "pF": (10 ** -12)
    }
    return value * multiplier[units]


if __name__ == "__main__":
    main()
