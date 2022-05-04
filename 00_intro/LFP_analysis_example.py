import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# load data:
mV = np.load('LFP_example_data.npy') # voltage signal, in mV
V = mV / 1000 # convert to V
npoints = len(V)
sampfreq = 1000 # Hz
t = np.arange(npoints) / sampfreq

# plot all data:
f1, a1 = plt.subplots(figsize=(10, 3)) # create a figure and axes
a1.plot(t, V, '-', c='black')
a1.set_xlim((t[0], t[-1])) # set hard x limits
a1.set_title('LFP example data')
a1.set_xlabel('Time (s)')
a1.set_ylabel('Volage (V)')

# calculate spectrogram using Welch's periodogram method:
winwidth = 5 # window width, seconds
winwidthsamples = int(winwidth * sampfreq)
P, freqs, t = mpl.mlab.specgram(V, winwidthsamples, sampfreq)

# set frequency limits:
fmin, fmax = 0, 50 # set frequency limits, in Hz
lo, hi = freqs.searchsorted([fmin, fmax])
P, freqs = P[lo:hi], freqs[lo:hi]

# convert power to dB and set power limits:
P = 10 * np.log10(P)
pmax = 200 # dB
P[P > pmax] = pmax

# plot the spectrogram:
f2, a2 = plt.subplots(figsize=(10, 3)) # create a figure and axes
P = P[::-1] # flip P array vertically for plotting
extent = t[0], t[-1], freqs[0], freqs[-1]
a2.imshow(P, extent=extent, cmap='hot') # plot power as an image
a2.axis('tight')
a2.set_xlabel('Time (s)')
a2.set_ylabel('Frequency (Hz)')
a2.set_title('LFP example spectrogram')
f2.tight_layout(pad=0.3) # crop figure to contents

# save power in dB to a file:
np.save('LFP_example_power_dB.npy', P)
