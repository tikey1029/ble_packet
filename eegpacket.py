a = []
eeg = {}
ecg = {}
chest = {}
left = {}
right = {}
breath = {}
x = 0
y = 0
z = 0
o = 0
p = 0
q = 0
times1 = 0
times2 = 0
times3 = 0
times4 = 0
times5 = 0
times6 = 0
#对比相邻封包的蓝牙Index差是否为1，判断蓝牙是否掉包
#包头为FE EF，包尾为EF FE，蓝牙的index为包头后第10和11位的2位16进制值
with open('0730', "r") as f:
	# a = f.readline().split(' ')
	# print(a)
	datas = f.readline()
	qwq = datas.replace('22 02', 'EF FE').replace('22 01', 'FE EF').replace('22 00', '22')
	a = qwq.split(' ')
	# print(a)

	if a[9] == '00':
		ecg[0] = a[11] + a[10]
		y = y+1
	elif a[9] == '01':
		eeg[0] = a[11] + a[10]
		x = x+1
	# elif a[9] == '02':
	# 	breath[0] = a[11] + a[10]
	# 	z = z+1
	elif a[9] == '03':
		chest[0] = a[11] + a[10]
		o = o+1
	# elif a[9] == '04':
	# 	left[0] = a[11] + a[10]
	# 	p = p+1
	# elif a[9] == '05':
	# 	right[0] = a[11] + a[10]
	# 	q = q+1

	for i in range(0, len(a)-14):
		if a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '01':
			eeg[x] = a[i+13] + a[i+12]
			if eeg[x] == 'FFFF':
				times1 = times1 + 1
			if x != 0:
				if (int(eeg[x],16) - int(eeg[x-1],16)) != 1:
					print(x)
			x = x+1
		elif a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '00':
			ecg[y] = a[i+13] + a[i+12]
			if ecg[y] == 'FFFF':
				times2 = times2 + 1
			y = y+1
		# elif a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '02':
		# 	breath[z] = a[i+13] + a[i+12]
		# 	if breath[z] == 'FFFF':
		# 		times3 = times3 + 1
			# if z != 0:
			# 	if (int(breath[z],16) - int(breath[z-1],16)) != 1:
			# 		print(z)
			# z = z+1
		elif a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '03':
			chest[o] = a[i+13] + a[i+12]
			if chest[o] == 'FFFF':
				times4 = times4 + 1
			o = o+1
		# elif a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '04':
		# 	left[p] = a[i+13] + a[i+12]
		# 	if left[p] == 'FFFF':
		# 		times5 = times5 + 1
			# if p != 0:
			# 	if (int(left[p],16) - int(left[p-1],16)) != 1:
			# 		print(p)
			# p = p+1
		# elif a[i] == 'FE' and a[i+1] == 'EF' and a[i+2] == 'EF' and a[i+3] == 'FE' and a[i+11] == '05':
		# 	right[q] = a[i+13] + a[i+12]
		# 	if right[q] == 'FFFF':
		# 		times6 = times6 + 1
		# 	q = q+1

eeg_all = int(eeg[x-1],16) - int(eeg[0],16) + 65535*times1 + 1
print('eeg_all =',eeg_all)
ecg_all = int(ecg[y-1],16) - int(ecg[0],16) + 65535*times2 + 1
print('ecg_all =',ecg_all)
# breath_all = int(breath[z-1],16) - int(breath[0],16) + 65535*times3 + 1
# print('breath_all =',breath_all)
chest_all = int(chest[o-1],16) - int(chest[0],16) + 65535*times4 + 1
print('chest_all =',chest_all)
# left_all = int(left[p-1],16) - int(left[0],16) + 65535*times5 + 1
# print('left_all =',left_all)
# right_all = int(right[q-1],16) - int(right[0],16) + 65535*times6 + 1
# print('right_all =',right_all)

print('eeg% =',(eeg_all-x)/eeg_all)
print('ecg% =',(ecg_all-y)/ecg_all)
# print('breath% =',(breath_all-z)/breath_all)
print('chest% =',(chest_all-o)/chest_all)
# print('left% =',(left_all-p)/left_all)
# print('right% =',(right_all-q)/right_all)
# print(eeg)
# print(eeg_all-x)
# print(len(eeg))
# print(breath)
# print(left)
# print(ecg)
# print(y)