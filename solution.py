#!/usr/bin/python

import math
import sys

#classes
# T CLASS -- Topic ID and Location ------------
class t_class:
	def __init__(self, in_string):
		inp = in_string.split(' ')
		self.topId = int(inp[0])
		self.topX = float(inp[1])
		self.topY = float(inp[2])


# Q CLASS -- Question ID and Associated Topics ---------
class q_class:
	def __init__(self, in_string):
		inp = in_string.split(' ')
		self.qId = int(inp[0])
		self.qN = int(inp[1])
		self.topIds = [0]*self.qN
		for i in range(2,self.qN+1):
			self.topIds[i-2] = int(inp[i])
	def __eq__(self, other):
		return self.qId == other

# N CLASS -- Query Type, Result Count, Query Location -----
class n_class:
	def __init__(self, in_string):
		inp = in_string.split(' ')
		self.rspTyp = inp[0]
		self.rspNum = int(inp[1])
		self.rspX = float(inp[2])
		self.rspY = float(inp[3])

#GlobContainers==========================
tlist = []
qlist = []
nlist = []

# Input parser ===================================
def get_input():
	global tlist 
	global qlist
	global nlist
	#fl = raw_input()
	f = open('random_input.txt', 'r+')  #TEMPLINE
	fl = f.readline()             #TEMPLINE
	fl_ = fl.split(' ')
	T = int(fl_[0])
	Q = int(fl_[1])
	N = int(fl_[2])

	tlist = [0]*T
	qlist = [0]*Q
	nlist = [0]*N
	#For T Lines 
		# TopicID TOPX TOPY
	#For Q Lines
		# ?ID Qn AssociatedTopicIDs[Qn]
	#For N Lines
		# RspType numResults LOCX LOCY
	for t in range(0,T):
		tlist[t] = t_class(f.readline())
	for q in range(0,Q):
		qlist[q] = q_class(f.readline())
	for n in range(0,N):
		nlist[n] = n_class(f.readline())



## DISTANCE FUNCTION -- TODO OPTIMIZE THIS
def dist(p0, p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

## OUTPUT SOLUTION FOR TOPIC QUERYS
def solve_t(inlist, rspNum):
	for idx in range(0,rspNum):
		sys.stdout.write('%d ' % inlist[idx].topId)
	sys.stdout.write('\n')

## OUTPUT SOLUTION FOR QUESTION QUERIES
def solve_q(inlist, rspNum, qstlist):
	count = 0
	for tops in inlist:
		for qstn in reversed(qstlist):
			if (count == rspNum):
				return
			if (tops.topId in qstn.topIds):
				qstlist.remove(qstn)
				sys.stdout.write('%d ' % qstn.qId)
				count += 1

## Stop here first to solve querys, dispatch to correct sub function
def solve_query(qIdx):
	global tlist
	global qlist
	global nlist

	n_ = nlist[qIdx]
	#for obj in tlist:
	#	obj.d = dist([n_.rspX, n_.rspY], [obj.topX, obj.topY]) 
	sortedlist = sorted(tlist, key=lambda t_class:  dist([n_.rspX, n_.rspY], [t_class.topX, t_class.topY]))	
	if (n_.rspTyp == 't'):
		solve_t(sortedlist, n_.rspNum)
	else:
		solve_q(sortedlist, n_.rspNum, qlist)

# The story begins here...
def main():
	get_input()
	for idx in range(0,len(nlist)):
		solve_query(idx)

if __name__ == "__main__":
	main()
