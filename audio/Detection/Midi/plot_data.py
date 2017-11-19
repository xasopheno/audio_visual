import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


data = np.genfromtxt('Detection/datasets/', delimiter=',', skip_header=10,
                     skip_footer=10, names=['x', 'y', 'z'])

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Mains power stability")
ax1.set_xlabel('time')
ax1.set_ylabel('Mains voltage')

ax1.plot(data['x'], data['y'], color='r', label='the data')
leg = ax1.legend()

plt.show()
