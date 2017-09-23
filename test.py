from spec_scale import scale as scale


def freq2name(freq):
	#print type(scale).__name__
	for k in scale:
		if scale[k][9][0] + 5 < freq :
			continue
		for (fq, index) in scale[k]:
			if abs(fq - freq) < 10:
				return k,index
	return 0,0

(k,v) = freq2name(430)
print k,v