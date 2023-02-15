import numpy
import scipy
from scipy import signal, fft
import matplotlib.pyplot as plt

n = 500
fs = 1000
f_max = 7
f_filter = 14

signal_gen = numpy.random.normal(0, 10, n)
time = numpy.arange(n) / fs  # n~sgen
w = f_max / (fs / 2)

filter = scipy.signal.butter(3, w, 'low', output='sos')
filter_signal = scipy.signal.sosfiltfilt(filter, signal_gen)
# fig 1
x1 = time
y1 = filter_signal
fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(x1, y1, linewidth=1)
ax.set_xlabel('Час (секунди)', fontsize=14)
ax.set_ylabel('Амлітуда сигналу', fontsize=14)
plt.title('Сигнал з максимальною частотою F_max = 7гц', fontsize=14)
title = 'fig1'
fig.savefig('./figures/' + title + '.png', dpi=600)

spectrum = scipy.fft.fft(filter_signal)  # розрахунок спектру
module_v = numpy.abs(scipy.fft.fftshift(spectrum))  # модульне значення
freq_rd_spec = scipy.fft.fftfreq(n, 1 / n)  # частотні відліки
freq_rd_c = scipy.fft.fftshift(freq_rd_spec)  # частотні відліки спектру
# fig 2
x2 = freq_rd_c
y2 = module_v
fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(x2, y2, linewidth=1)

ax.set_xlabel('Частота (Гц)', fontsize=14)
ax.set_ylabel('Амлітуда сигналу', fontsize=14)

plt.title('Спектр сигналу з максимальною частотою F_max = 7гц', fontsize=14)
title2 = 'fig2'
fig.savefig('./figures/' + title2 + '.png', dpi=600)

# discrete_signal = numpy.zeros(n)
discrete_signals = []
discrete_spectrums = []

w2 = f_filter/(fs/2)
filter_discrete = scipy.signal.butter(3, w2, 'low', output='sos')
discrete_signals_filtred = []

dispersion_s = []
snr_s = []

for d_t in [2, 4, 8, 16]:
    discrete_signal = numpy.zeros(n)

    for i in range(0, round(n / d_t)):
        discrete_signal[i * d_t] = filter_signal[i * d_t]
    discrete_signals += [list(discrete_signal)]

    discrete_spectrum = fft.fft(discrete_signal)
    module_s = numpy.abs(scipy.fft.fftshift(discrete_spectrum))
    discrete_spectrums += [list(module_s)]

    discrete_signal_filtred = scipy.signal.sosfiltfilt(filter_discrete, discrete_signals)
    discrete_signals_filtred += [list(discrete_signal_filtred)]



    e1 = discrete_signal_filtred - filter_signal
    dispersion = numpy.var(e1)
    snr = numpy.var(filter_signal) / dispersion
    dispersion_s += [dispersion]
    snr_s += [snr]


x3 = time
y3 = discrete_signals

fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))

s = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(x3, y3[s], linewidth=1)
        s += 1

fig.supxlabel('Час (секунди)', fontsize=14)
fig.supylabel('Амлітуда сигналу', fontsize=14)
fig.suptitle('Сигнал с кроком дискретизації Dt = (2, 4, 8, 16)', fontsize=14)
title3 = 'pr3_fig3'
fig.savefig('./figures/' + title3 + '.png', dpi=600)

x4 = freq_rd_c
y4 = discrete_spectrums

fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))

s2 = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(x4, y4[s2], linewidth=1)
        s2 += 1

fig.supxlabel('Частота (Гц)', fontsize=14)
fig.supylabel('Амлітуда спектру', fontsize=14)
fig.suptitle('Спектри сигналів з кроком дискретизації Dt = (2, 4, 8, 16)', fontsize=14)
title4 = 'pr3_fig4'
fig.savefig('./figures/' + title4 + '.png', dpi=600)


x5 = time
y5 = discrete_signal_filtred

fig, ax = plt.subplots(2, 2, figsize=(21 / 2.54, 14 / 2.54))

s3 = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax[i][j].plot(x5, y5[s3], linewidth=1)
        s3 += 1


fig.supxlabel('Час секунди', fontsize=14)
fig.supylabel('Амлітуда сигналу', fontsize=14)
fig.suptitle('Спектри сигналів з кроком дискретизації Dt = (2, 4, 8, 16)', fontsize=14)
title5 = 'pr3_fig5'
fig.savefig('./figures/' + title5 + '.png', dpi=600)


x6 = [2, 4, 8, 16]
y6 = dispersion_s
fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(x6, y6, linewidth=1)
ax.set_xlabel('Крок дискретизації', fontsize=14)
ax.set_ylabel('Дисперсія', fontsize=14)
plt.title('Залежність дисперсії від кроку дискретизації', fontsize=14)
title = 'pr3_fig6'
fig.savefig('./figures/' + title + '.png', dpi=600)


x7 = [2, 4, 8, 16]
y7 = snr_s
fig, ax = plt.subplots(figsize=(21 / 2.54, 14 / 2.54))
ax.plot(x7, y7, linewidth=1)
ax.set_xlabel('Залежність співвідношення сигнал-шум від кроку дискретизації', fontsize=14)
ax.set_ylabel('ССШ', fontsize=14)
plt.title('Залежність дисперсії від кроку дискретизації', fontsize=14)
title = 'pr3_fig7'
fig.savefig('./figures/' + title + '.png', dpi=600)
