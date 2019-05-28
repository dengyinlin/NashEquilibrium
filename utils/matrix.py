import numpy as np

class Matrix:

	def __init__(self, row, col, A):
		self.row = row
		self.col = col
		self.A, self.B = np.vsplit(A, 2)
		#print("matrixA:\n",self.A, "\nmatrixB:\n",self.B)

	def cond_dominate(self, a, b): # if a >= b: return true
		x = a.shape[0]
		for i in range(x):
			if a[i] < b[i]:
				return 0
		return 1

	def rdom(self, S1, S2):
		C = self.A[S1]
		C = C[:,S2]
		x = C.shape[0]

		for i in range(x):
			for j in range(x):
				if i == j:
					continue
				if self.cond_dominate(C[i], C[j]):
					return 0
		return 1

	def dominate_row(self, S1, S2):
		C = self.A[S1]
		C = C[:,S2]
		x = C.shape[0]

		flag = np.zeros(x, dtype=int)
		for i in range(x):
			for j in range(x):
				if flag[j] or i == j:
					continue
				if self.cond_dominate(C[i], C[j]):
					flag[j] = 1
		res = []
		for i in range(x):
			if flag[i] == 0:
				res.append(S1[i])
		if len(res) == 0:
			res.append(S1[0])
		res = np.array(res)
		return res

	def dominate_col(self, S1, S2):
		C = self.B[S1]
		C = C[:, S2]
		C = C.T
		S1, S2 = S2, S1
		x = C.shape[0]
		flag = np.zeros(x, dtype=int)
		for i in range(x):
			for j in range(x):
				if flag[j] or i == j:
					continue
				if self.cond_dominate(C[i], C[j]):
					flag[j] = 1
		res = []
		for i in range(x):
			if flag[i] == 0:
				res.append(S1[i])
		if len(res) == 0:
			res.append(S1[0])
		res = np.array(res)
		return res
				
