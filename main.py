import numpy as np
import os
from utils import matrix as M
from itertools import combinations
from utils import lp
import time
import signal

def readsol(filename):
	with open(filename) as f:
		# read row and column
		l = f.readline()
		l = l.split(' ')
		row = int(l[0])
		col = int(l[1])
		#print("row =", row, "col =", col)
		# solve matrix data
		lines = f.readlines()
		A = np.zeros((row*2, col), dtype=float)
		A_row = 0
		for line in lines:
			_list = line.strip('\n').split(' ')
			A[A_row:] = _list[0:col]
			A_row += 1
		#print(A)
		#build matrix
		game = M.Matrix(row, col, A)
		#print("readsol finished")
		return game


def solve(x1, x2, G):
	r = [i for i in range(G.row)]
	c = [j for j in range(G.col)]
	#print("x1=",x1, x2, r)
	for x in combinations(r, x1):
		S1 = np.array(x, dtype = int)
		A2 = G.dominate_col(S1, c)
		#print(x, S1)
		#print(S1, A2)
		if G.rdom(S1, A2):
			for y in combinations(A2, x2):
				S2 = np.array(y, dtype = int)
				if G.rdom(S1, S2):					
					if lp.solveLP(G.A, G.B, S1, S2, G.row, G.col):
						#print("solution = ", S1, S2)
						return 1


def handler(signum, frame):
	raise Exception("timeout")

def Game(gameMatrix):
	for t in range(gameMatrix.row+1):
		for d in range(1, 2*gameMatrix.row+1):
		# |x1-x2|=t, x1+x2=d, assume x1 > x2 and swap
			if (d+t)%2 == 0:
				x1 = int((d+t)/2)
				x2 = d-x1
				if x1 > 0 and x2 > 0:
					if x1 <= gameMatrix.row and x2 <= gameMatrix.col:
						if solve(x1, x2, gameMatrix):
							return True
							
					if x1 != x2 and x2 <= gameMatrix.row and x1 <= gameMatrix.col:
						if solve(x2, x1, gameMatrix):
							return True
	return False
# Main
filedir = './data/'
filelist = os.listdir(filedir)
print(filelist)

cnt = 0
tot = 0
for name in filelist:
	tot = tot + 1
	gameMatrix = readsol(filedir+name)
	print(name)
	try:
		signal.signal(signal.SIGALRM, handler)
		signal.alarm(1)
		flag = Game(gameMatrix)
		if falg == False:
			print("why not found!?!")
		cnt = cnt + 1
		print(str(cnt) + "/ " + str(tot))
	except :
		print("time out")
		

print(str(cnt) + "/ " + str(tot))
print(cnt/tot)
print("\n")
