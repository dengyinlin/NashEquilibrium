import pulp
from itertools import combinations
import numpy as np

def solveLP(A, B, S1, S2, rows, cols):
	R = ["x"+str(i) for i in S1]
	C = ["y"+str(j) for j in S2]
	
	x = pulp.LpVariable.dicts('table', R, lowBound = 0, upBound = 1)
	y = pulp.LpVariable.dicts('table', C, lowBound = 0, upBound = 1)
	v1 = pulp.LpVariable("v1", 0, None)
	v2 = pulp.LpVariable("v2", 0,  None)
	
	model = pulp.LpProblem("NE feasibility", pulp.LpMaximize)
	
	model += v1 + v2
	
	for i in range(rows):
		model += sum(A[i][j] * y["y"+str(j)] for j in S2) <= v1
	
	for i in S1:
		model += sum(A[i][j] * y["y"+str(j)] for j in S2) >= v1
		
	for j in range(cols):
		model += sum(B[i][j] * x["x"+str(i)] for i in S1) <= v2
	for j in S2:
		model += sum(B[i][j] * x["x"+str(i)] for i in S1) >= v2
		
	model += sum(x[ri] for ri in R) == 1 
	model += sum(y[ci] for ci in C) == 1 
	
	try:
		model.solve()
	except Exception:
		#print("infeasible")
		return False

	if model.status == -1:
		#print("infeasible")
		return False
	
	x_star = list(map(lambda ri: x["x"+str(ri)].value() if ri in S1 else 0, range(rows)))
	y_star = list(map(lambda ci: y["y"+str(ci)].value() if ci in S2 else 0, range(cols)))
	
	#print("final value: " + str(v1.value()) + " " + str(v2.value()))
	#print(x_star)
	#print(y_star)
	
	r = np.dot(np.array(A), np.array(y_star))
	vr = np.full((rows,), v1.value() + 1e-4)
	print(r)
	print(vr)
	#assert((r <= vr).all())
	#assert(np.sum(x_star) == 1)
	
	c = np.dot(np.array(B).T, np.array(x_star))
	vc = np.full((cols,), v2.value() + 1e-4)
	#print(c)
	#print(vc)
	#assert((c <= vc).all())
	#assert(np.sum(y_star) == 1)
	
	return True
'''
rows = 10
cols = 10
r = [i for i in range(rows)]
c = [j for j in range(cols)]
#A = [[4, 1], [2, 3]]
#B = [[4, 2], [1, 3]]
#solveLP(A,B,[1,], [1,], 2,2)
#A = np.random.rand(rows, cols)
#B = np.random.rand(rows, cols)
A = np.random.randint(0, 5, (rows, cols))
B = np.random.randint(0, 5, (rows, cols))

for k in range(5):
	for S1 in combinations(r, k):
		for S2 in combinations(c, k):
			if (solveLP(A, B, S1, S2, rows, cols)):
				break
'''
