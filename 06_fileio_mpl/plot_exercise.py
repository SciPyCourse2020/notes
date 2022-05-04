import numpy as np
import matplotlib.pyplot as plt

# get data:
t = np.arange(0, 4*np.pi+0.1, 0.1)
s = np.sin(t)
c = np.cos(t)

# plot the data as lines:
plt.figure()
plt.plot(t, s, label='sin', marker='')
plt.plot(t, c, label='cos', marker='')
plt.xlabel('Time (s)')
plt.ylabel('Position')
plt.legend(loc='upper right')
plt.show()
plt.savefig('sin and cos vs t.png')

# plot the distributions of the data:
plt.figure()
plt.hist(s, bins=20, label='sin')
plt.hist(c, bins=20, label='cos')
plt.xlabel('Position')
plt.legend()
plt.show()
plt.savefig('distribution.png')
