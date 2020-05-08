import math
from random import random

import matplotlib.pyplot as plt
import numpy as np
from time import time
from decimal import Decimal

n = 10
N = 256
w = 900


def time_counter(callback, *args):
    start = time()
    callback(*args)
    end = time()
    return end - start


def signal():
    signal = []
    for i in range(N):
        signal_point = 0
        for j in range(n):
            signal_point += random()*math.sin(w/n*((j+1)*i)+random())
        signal.append(signal_point)
    return signal


def Fx(signal):
    fx = []
    for p in range(N):
        fi_1 = 0
        fi_2 = 0
        fr_1 = 0
        fr_2 = 0
        for k in range(int(N/2)-1):
            fi_1 += signal[2*k]*math.sin((4*math.pi*p*k)/N)
            fr_1 += signal[2*k]*math.cos((4*math.pi*p*k)/N)
            fi_2 += signal[2*k+1]*math.sin((2*math.pi*p*(k*2+1))/N)
            fr_2 += signal[2*k+1]*math.cos((2*math.pi*p*(k*2+1))/N)
        fx.append(math.sqrt(math.pow(fr_1+fr_2, 2)+math.pow(fi_1+fi_2, 2)))
    return fx


def main():
    sig = signal()
    fx = Fx(sig)
    fxx = np.fft.fft(sig)
    plt.figure(1)
    plt.plot(range(N), fx)
    plt.figure(2)
    plt.plot(range(N), fxx)
    plt.show()
    fx_time = time_counter(Fx, sig)
    fxx_time = Decimal(time_counter(np.fft.fft, sig))
    print(f"FFT calculating time: {fx_time} sec")
    print(f"FFT from numpy calculating time: {fxx_time} sec")
    print(f'{"FFT" if fx_time < fxx_time else "FFT from numpy"} is faster than')


main()
