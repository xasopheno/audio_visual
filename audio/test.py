import matplotlib.pyplot as plt
import numpy as np

sample_rate = 100 * 2
freq = 5
freq2 = 7
x = np.arange(sample_rate)
y = np.sin(2 * np.pi * freq * x / sample_rate)
plt.plot(x + 50, y)
plt.xlabel('time')
plt.ylabel('sample(n)')
plt.show()


# from pylab import *
#
# sample_rate = .001
# f0, f1 = 10, 20
# t_change = 2
#
# times = arange(0, 4, sample_rate)
#
# ramp = 1./(1+exp(-6.*(times-t_change)))
# freq = f0*(1-ramp)+f1*ramp
# phase_correction = add.accumulate(times*concatenate((zeros(1), 2*pi*(freq[:-1]-freq[1:]))))
#
# figure()
# subplot(311)
# plot(times, freq)
# subplot(312)
# plot(times, sin(2*pi*freq*times))
# subplot(313)
# plot(times, sin(2*pi*freq*times+phase_correction))
#
# show()
