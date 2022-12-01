#!/usr/bin/python3

# William Moody (@bmdyy)
# 30.11.2022

for i in range(40):
	l = 2 + 20*i
	h = 21 + 20*i
	print("%d\t=MIN(C%d:C%d)\t=AVERAGE(C%d:C%d)\t=MAX(C%d:C%d)\t=MIN(D%d:D%d)\t=AVERAGE(D%d:D%d)\t=MAX(D%d:D%d)" % (i+1, l,h, l,h, l,h, l,h, l,h, l,h))
