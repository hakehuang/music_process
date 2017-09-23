import sys
import copy
from spec_scale import scale

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft
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
plot_x = []
plot_y = [[], [], [], [], [], [],
          [], [], [], [], [], [],
          [], [], [], [], [], []]

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
	#index = np.argmax(abs(c[:(len(c)/2-1)]/step))
	list = abs(c[:(len(c)/2-1)]/step)
	new_list = copy.deepcopy(list)
	new_list.sort()
	print('time %d'%(time_stamp))
	plot_x.insert(len(plot_x),time_stamp)
	#plot_x.insert(len(plot_x),time_stamp + step*100/fs - 1)
	ii = 0
	plot_count += 1
	plt.ylabel("freq",fontsize=14)
	plt.xlabel("ms",fontsize=14)
	#plt.ylim([0, 2300])
	for k in reversed(new_list[-6:]):
		kindex = np.where(list==k)
		#print kindex
		#print type(kindex).__name__
		# if type(kindex).__name__ == "tuple":
		# 	continue
		if new_list[-1] > 0.001:
			try:
				print('%s:%f:%d'%("\t",k,freqArray[kindex]))
				(kii,vii) = freq2name(freqArray[kindex])
				print(kii,vii)
				plot_y[ii].insert(len(plot_y[ii]), freqArray[kindex])
				#plot_y[ii].insert(len(plot_y[ii]), freqArray[kindex])
				ii += 1
			except:
				plot_y[ii].insert(len(plot_y[ii]), 0)
				ii += 1
				print ""
		else:
			plot_y[ii].insert(len(plot_y[ii]), 0)
			ii += 1
			print ""			

	i = i + step
	if plot_count == 120:	
		if plot_y[1]:
			plt.plot(plot_x, plot_y[1], '*')
		# if plot_y[2]:
		# 	plt.plot(plot_x, plot_y[2], '*')
		# if plot_y[3]:
		# 	plt.plot(plot_x, plot_y[3], '*')
		# if plot_y[4]:
		# 	plt.plot(plot_x, plot_y[4], '*')
		# if plot_y[5]:
		# 	plt.plot(plot_x, plot_y[5], '*')
		# if plot_y[6]:
		# 	plt.plot(plot_x, plot_y[6], '*')
		# if plot_y[7]:
		# 	plt.plot(plot_x, plot_y[7], '*')
		# if plot_y[8]:
		# 	plt.plot(plot_x, plot_y[8], '*')
		# if plot_y[9]:
		# 	plt.plot(plot_x, plot_y[9], '*')
		# if plot_y[10]:
		# 	plt.plot(plot_x, plot_y[10], '*')
		# if plot_y[11]:
		# 	plt.plot(plot_x, plot_y[11], '*')
		# if plot_y[12]:
		# 	plt.plot(plot_x, plot_y[12], '*')
		# if plot_y[13]:
		# 	plt.plot(plot_x, plot_y[13], '*')
		# if plot_y[14]:
		# 	plt.plot(plot_x, plot_y[14], '*')
		# if plot_y[15]:
		# 	plt.plot(plot_x, plot_y[15], '*')
		# if plot_y[16]:
		# 	plt.plot(plot_x, plot_y[16], '*')
		# if plot_y[17]:
		# 	plt.plot(plot_x, plot_y[17], '*')
		if plot_y[0]:
			plt.plot(plot_x, plot_y[0], '*')
		plt.show()
		#print plot_x
		#print plot_y
		plot_count = 0
		plot_x = []
		plot_y = [[], [], [], [], [], [],
          [], [], [], [], [], [],
          [], [], [], [], [], []]
	#raw_input()