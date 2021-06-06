from thinkdsp import CosSignal, SinSignal 
from thinkdsp import decorate
import matplotlib.pyplot as plt
cos_sig = CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)

mix = sin_sig + cos_sig 
wave = mix.make_wave(duration=0.01, start=0, framerate=11025)
wave.play('test3.wav')
wave.normalize()
wave.make_audio()
plt.subplot(2,1,1)
wave.plot()
spectrum = wave.make_spectrum()
plt.subplot(2,1,2)
spectrum.plot(high=5000)
decorate(xlabel='Frequency (Hz)')
plt.show()
