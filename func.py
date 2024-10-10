import matplotlib.pyplot as plt
def process(f, sid, time, vd, temp):
	#extracts all IDs, vd and temp
	for line in f:
		data = line.split(',')
		#print(int(data[0].split(':')[1]))
		sid.append(int(data[0].split(':')[1]))
		#print(float(data[2].split(':')[1]))
		vd.append(float(data[2].split(':')[1]))
		#print(float(data[4].split(':')[1].split("}")[0]))
		temp.append(float(data[4].split(':')[1].split("}")[0]))
	#check if need to remove 172
	for i in range(0, 4):
		if sid[i] is not 172:
			remove_172(sid, vd, temp)
			break
	#print(vd)
	construct_time(sid, time)
def construct_time(sid, time):
	i = 0
	for j in sid:
		time.append(i)
		i += 0.5
def remove_172(sid, vd, temp):
	i = 0
	while (i < len(sid)):
		#177 was measured with negative voltage drop
		if (sid[i] is 177):
			vd[i] = vd[i] * -1
		if ((sid[i] is 172) or (sid[i] is 0)):
			sid.pop(i)
			vd.pop(i)
			temp.pop(i)
			i -= 1
		i += 1
def generate_plot(file):
	sid = []	
	temp = []
	vd = []
	time = []
	with open(file, 'r') as f:
	    process(f, sid, time, vd, temp)
	SSU = file.split('.')[0].split('t')[1]
	plt.figure()
	plt.suptitle('SSU No.' + SSU)
	plt.subplot(211)
	plt.plot(time, vd, 'r-', linewidth=0.5)
	plt.ylabel('Voltage drop / mV')
	#plt.axis([xmin, xmax, ymin, ymax])
	if (len(time) > 1200):
		plt.axis([0, 800, 0.3, 0.7])
	else:
		plt.axis([0, 400, 0.3, 0.7])
 
	plt.subplot(212)
	plt.plot(time, temp, 'b-', linewidth=0.5)
	plt.ylabel('Temperature / C')
	plt.xlabel('Time / s')
	if (len(time) > 1200):
		plt.axis([0, 800, 0, 100])
	else:
		plt.axis([0, 400, 0, 100])
	#plt.show()
	plt.savefig(SSU + '.png', bbox_inches='tight')
 
 
#generate_plot('heat55.txt')
 
 
 
 
 
 
