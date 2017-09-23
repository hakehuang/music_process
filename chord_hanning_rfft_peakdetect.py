
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.signal import hann
#follow the guide on 
#http://simplsound.sourceforge.net/
import simpl
import simpl.peak_detection as peak_detection

PeakDetection = peak_detection.PeakDetection
SMSPeakDetection = peak_detection.SMSPeakDetection
SndObjPeakDetection = peak_detection.SndObjPeakDetection

fs, data = read("c:/temp/test.wav") # load the data
a = data.T[0] # this is a two channel soundtrack

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

plot_count = 0
window = hann(step)
pd = SndObjPeakDetection()
pd.max_peaks = 20
while i < len(a) - step:
	d = []
	time_stamp = i*100/fs #in ms
	c = a[i:i+step]
	# calculate fourier transform (complex numbers list)
	pks = pd.find_peaks(c)
	simpl.plot.plot_partials(partls)
	# set title and label axes
	plt.title("Flute Partials")
	plt.ylabel("Frequency (Hz)")
	plt.xlabel("Frame Number")

	print('time %d'%(time_stamp))
	plot_count += 1
	i = i + step
	if plot_count == 120:	
		plt.show()
		plot_count = 0

	#raw_input()