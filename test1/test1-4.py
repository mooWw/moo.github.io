import os
import matplotlib.pyplot as plt
from thinkdsp import read_wave
from thinkdsp import decorate
from IPython.display import display
from thinkdsp import SinSignal

wave3 = read_wave('test.wav')
wave3.normalize()
wave3.make_audio()

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave3, 0.3)
wave3.make_audio()
wave3.plot()

wave3.write(filename='test4.wav')
plt.show()