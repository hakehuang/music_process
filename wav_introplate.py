import sys
import copy


import numpy as np
import math
from scipy.misc import central_diff_weights 
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api


#from scipy.interpolate import UnivariateSpline
fs, data = wavfile.read("c:/temp/06DieWasserflut.wav") # load the data
a = data.T[0] # this is a two channel soundtrack, I get the first track
b=[(ele/2**16.)*2-1 for ele in a] # this is 16-bit track, b is now normalized on [-1,1)
i = 0
w1 = central_diff_weights(49, 1)
step = 4096


def freq2scale(freq):
	return 69 + 12 * math.log(freq, 2)

print(fs)
print("===========")
print("time in ms:intense:freq:name")
plot_x = []
plot_y = []
plot_count = 0
while i < len(a) - step:
	d = []
	time_stamp = i*100/fs #in ms
	c = fft(a[i:i+step]) # calculate fourier transform (complex numbers list)
	d.append(c)  # you only need half of the fft list (real signal symmetry)
	#print c[0]
	freqArray = np.arange(0, step/2 - 1, 1.0) * (fs / step);
	#print freqArray
	sys.stdout.flush()
	#plt.plot(freqArray[:(len(c)/2-1)], abs(c[:(len(c)/2-1)]/step)) 
	#plt.show()
	index = np.argmax(abs(c[:(len(c)/2-1)]/step))
	mags = abs(c[:(len(c)/2-1)]/step)
	mags = 20 * scipy.log10(mags)
	mags -= max(mags)
	try:
		print('%d:%f:%d'%(time_stamp,mags[index],freqArray[index]))
	except:
		print ""
	i = i + step
	plot_count += 1
	plt.ylabel("intense",fontsize=14)
	plt.xlabel("ms",fontsize=14)
	#plt.ylim([0, 0.1])
	plot_x.insert(len(plot_x),time_stamp)
	plot_x.insert(len(plot_x),time_stamp + step*100/fs - 1)
	plot_y.insert(len(plot_y), list_abs[index])
	plot_y.insert(len(plot_y), list_abs[index])
	#https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html
	if plot_count == 50:
		#x = np.linspace(-5, 5, 100)
		#dx_calc = np.convolve(w1[::-1], plot_y, 'same')
		log_plot_y = [np.log10(y) for y in plot_y ]
		z1 = np.polyfit(plot_x, log_plot_y, 3)
		p1 = np.poly1d(z1)
		#xs = np.linspace()
		#print(spl)
		plt.plot(plot_x, p1(plot_x), 'r', label="plotfit")
		plt.plot(plot_x, log_plot_y, '*', label="orginal")
		#plt.plot(plot_x, dx_calc, 'g-o', label="diff")
		plt.legend(loc=4)
		plt.title('polyfitting')
		plt.show()
		#print plot_x
		#print plot_y
		plot_count = 0
		plot_x = []
		plot_y = []
	#raw_input()
