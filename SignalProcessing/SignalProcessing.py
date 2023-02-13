import numpy
import scipy
from scipy import signal, fft
import matplotlib.pyplot as plt


n = 500
fs = 1000
f_max = 7

signal_gen = numpy.random.normal(0, 10, n)
time = numpy.arange(n)/fs      #n~sgen
w = f_max/(fs/2)

filter = scipy.signal.butter(3, w, 'low', output='sos')
filter_signal = scipy.signal.sosfiltfilt(filter, signal_gen)

x1 = time
y1 = filter_signal
fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(x1, y1, linewidth=1)
ax.set_xlabel('Час (секунди)', fontsize=14)
ax.set_ylabel('Амлітуда сигналу', fontsize=14)
plt.title('Сигнал з максимальною частотою F_max = 7гц', fontsize=14)
title = 'fig1'
fig.savefig('./figures/' + title + '.png', dpi=600)


spectrum = scipy.fft.fft(filter_signal)
module_v = numpy.abs(scipy.fft.fftshift(spectrum))
freq_rd_spec = scipy.fft.fftfreq(n, 1/n)
freq_rd_c = scipy.fft.fftshift(freq_rd_spec)

x2 = freq_rd_c
y2 = module_v
fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(x2, y2, linewidth=1)

ax.set_xlabel('Частота (Гц)', fontsize=14)
ax.set_ylabel('Амлітуда сигналу', fontsize=14)

plt.title('Спектр сигналу з максимальною частотою F_max = 7гц', fontsize=14)
title2 = 'fig2'
fig.savefig('./figures/' + title2 + '.png', dpi=600)
