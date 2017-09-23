
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.signal import hann
#follow the guide on 
#http://simplsound.sourceforge.net/
from modal.onsetdetection import OnsetDetection
from modal.detectionfunctions import ComplexODF
from modal.ui.plot import (plot_detection_function,plot_onsets)
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# read audio file
audio = read("c:/temp/test.wav")[1]
# values between -1 and 1
audio = audio / 32768.0
# create detection function
codf = ComplexODF()
odf = codf.process(audio)
# create onset detection object
od = OnsetDetection()
hop_size = codf.get_hop_size()
onsets = od.find_onsets(odf)*hop_size
# plot onset detection results
plt.subplot(2,1,1)
plt.title("Audio And Detected Onsets")
plt.ylabel("Sample Value")
plt.xlabel("Sample Number")
plt.plot(audio, "0.4")
plot_onsets(onsets)
plt.subplot(2,1,2)
plt.title("Detection Function And Threshold")
plt.ylabel("Detection Function Value")
plt.xlabel("Sample Number")
plot_detection_function(odf, hop_size)
thresh = od.threshold
plot_detection_function(thresh, hop_size,"green")
plt.show()
