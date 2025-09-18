#!/usr/bin/env python3

import math

F = 1000
Zf = 2.9 # Resistance on frequency 'F'
Re = 0.3 # Resistance on frequency 0Hz (measurement by multimeter)

Xl = math.sqrt(Zf ** 2 - Re ** 2)
L = Xl / (2*math.pi * F)

print("L: {:.2f} mH".format(L*1000))

# Предполагаемы объем корпуса
V=7

Qts=0.47
Vas=4.63
Fs=64
Fc=Fs*math.sqrt(1+Vas/V)

# Добротность в предполагаемом объеме V
Qtc=Fc/(Fs/Qts)

print()
print("--- Free air params ---")
print("V: -")
print("Fs: {:.2f} Hz".format(Fs))
print("Qts: {:.2f}".format(Qts))
print()
print("--- Expected params in box".format(V))
print("V: {:.2f} L".format(V))
print("Fc: {:.2f} Hz".format(Fc))
print("Qtc: {:.2f}".format(Qtc))
