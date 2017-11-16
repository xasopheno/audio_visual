import numpy as np
data = np.genfromtxt('rounded.csv', delimiter=',',
                     skip_footer=10, names=['num', 'length'])

ax1.plot(data['x'], data['y'], color='r', label='the data')
