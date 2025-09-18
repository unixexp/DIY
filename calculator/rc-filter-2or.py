import math
from webbrowser import Error


def main():
    # Maximum Pass-band Ripple [dB]
    Amax = 1.5
    # Minimum Stop-band Attenuation [dB]
    Amin = 16
    # Cutoff Frequency
    Fc = 100

    Fs = Fc * 4

    # Calculate necessary filter order
    Ep = math.sqrt(10**(Amax / 10) - 1)
    Es = math.sqrt(10**(Amin / 10) - 1)
    n = math.log(Es / Ep) / math.log(Fs / Fc)
    n = math.ceil(n)
    wc = 2 * math.pi * Fc

    # Component values
    #R1 = R2 = 39000
    R1 = R2 = 0
    C1 = to_farads(22, "nF") # C10
    C2 = to_farads(10, "nF") # C9
    #C1 = C2 = to_farads(2.2, "nF")

    if R1 != 0 and R2 != 0:
        C1 = (1 / (R1 * wc)) * 2.613
        C2 = (1 / (R2 * wc)) * 0.382
    elif C1 != 0 and C2 != 0:
        R1 = (1 / (C1 * wc)) * 1.414
        R2 = (1 / (C2 * wc)) * 0.7071
    else:
        print("Please set start values of R1,R2 or C1,C2")
        exit(1)

    Fc1 = int(1 / (2 * math.pi * R1 * C1))
    Fc2 = int(1 / (2 * math.pi * R2 * C2))

    # Actual Stop-band Attenuation
    Fp = Fc * (Ep ** (1/n))
    Amin_test_1 = math.floor(10 * math.log10( 1 + Ep**2 * (Fs/Fp)**(2*n) ))
    Amin_test_2 = math.floor(10 * math.log10( 1 + (Fs/Fc)**(2*n) ))

    print("Cut-off Frequency: {} Hz".format(Fc))
    print("Stop-band Frequency: {} Hz".format(Fs))
    print("Pass-band Frequency where gain is [-{} dB]: {} Hz".format(Amax, int(Fp)))
    print("Actual Stop-band Attenuation: {} dB"
          .format(Amin_test_1 if Amin_test_1 == Amin_test_2 else "!!! Test failed {} != {}".format(Amin_test_1,
                                                                                                   Amin_test_2)))
    print("Filter order: {}".format(n))

    print("\n-- 1-st RC figure setup [{} Hz] --".format(Fc1))
    print("R1: {} Ohm".format(int(R1)))
    print("C1: {:.2f} nF".format(C1 * (10 ** 9)))
    print("\n-- 2-st RC figure setup [{} Hz]--".format(Fc2))
    print("R2: {} Ohm".format(int(R2)))
    print("C2: {:.2f} nF".format(C2 * (10 ** 9)))


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
