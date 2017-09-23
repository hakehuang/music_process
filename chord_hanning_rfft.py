import sys
import copy
import scipy

from spec_scale import scale
from scipy.signal import hann
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fftpack import rfft
from scipy.io import wavfile # get the api
fs, data = wavfile.read("c:/temp/test.wav") # load the data
a = data.T[0] # this is a two channel soundtrack, I get the first track
b=[(ele/2**16.)*2-1 for ele in a] # this is 16-bit track, b is now normalized on [-1,1)
i = 0

step = 1024

def freq2scale(freq):
	return 69 + 12 * math.log(freq, 2)

def freq2name(freq):
	#print type(scale).__name__
	for k in scale:
		if int(scale[k][9][0]) + 5 < freq :
			continue
		for (fq, index) in scale[k]:
			if abs(fq - freq) < 30:
				return k,index
	print(int(scale[k][9][0]))
	return 0,0

print(fs)
print("===========")
print("time in ms:intense:freq")


plot_count = 0
window = hann(step)
while i < len(a) - step:
	d = []
	time_stamp = i*100/fs #in ms
	c = a[i:i+step]*window
	# calculate fourier transform (complex numbers list)
	mags = abs(rfft(c))
	# convert to dB
	mags = 20 * scipy.log10(mags)
	# normalise to 0 dB max
	mags -= max(mags)
	# plot

	print('time %d'%(time_stamp))
	#plot_x.insert(len(plot_x),time_stamp + step*100/fs - 1)
	plt.plot(mags)
	plot_count += 1
	plt.ylabel("Magnitude (dB)",fontsize=14)
	plt.xlabel("Frequency Bin",fontsize=14)
	i = i + step
	if plot_count == 120:	
		plt.show()
		plot_count = 0

	#raw_input()