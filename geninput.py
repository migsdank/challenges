#!/usr/bin/python

import random

T = random.randrange(1,10000)
Q = random.randrange(1,1000)
N = random.randrange(1,10000) 

f = open('random_input.txt', 'w+')

out = str(T) + ' ' + str(Q) + ' ' + str(N) + '\n'
f.write(out)

for t in range(0,T):
	tId = t
	tX = random.uniform(0,1000000.0)
	tY = random.uniform(0,1000000.0)
	out = str(tId) + str(' ') + str(tX) + str(' ') + str(tY)	+ str('\n')
	f.write(out)


for q in range(0,Q):
	qId = q
	qN = random.randrange(0, 10)
	topIds = [0]*qN

	out = str(qId) + str(' ') + str(qN) + str(' ')
	for idx in range(0,qN):
		out += str(random.randrange(0,T-1))
		out += str(' ')
	out += str('\n')
	f.write(out)

for n in range(0,N):
	coin = random.randrange(0,2)
	if (coin):
		out = str('t ')
	else:
		out = str('q ')

	results = random.randrange(0,100)
	resY = random.uniform(0,1000000.0)
	resX = random.uniform(0,1000000.0)
	
	out += str(results) + ' ' + str(resX) + ' ' + str(resY) + '\n'
	f.write(out)


f.close()
