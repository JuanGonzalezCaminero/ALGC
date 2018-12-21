import random
#This algorithm has no practical utility
#We want to verify if C = AB, being C, A and B n x n matrices
#To do so, Instead of doing AB and comparing it to C, we can consider
#D = AB - C. If some row in D is not-null, we will know for a fact that
#AB != C. We take N rows from D, representing the selected rows with an array
#of length n, which has a 0 or a 1 in each position. with a probability of 50%
#for selecting each row.
#We can get D by doing AB - C, but that is the same as the first case, however,
#If we calculate the sum of the rows in D and store the result for each row in 
#an array, that is the same as doing XD, being X the array indicating wether we select
#a row or not. This result is the same, of course, ad doing X(AB - C), thus, if
#XAB = XC, we will know that, with a probability of 50%, AB = C.
#If we calculate XAB in the order (XA)B, the number of operations needed is drastically
#reduced.
#If the algorithm says they are not equal we now it's true, else, we know they are equal
#with a probability of 50%. We can improve that number calling the algorithm multiple times

A = [[1, 2, 3], 
	 [4, 5, 6], 
	 [7, 8, 9]]

#B = [[1, 0, 0],
#	 [0, 1, 0], 
#	 [0, 0, 1]]

#C = [[1, 2, 3], 
#	 [4, 5, 6], 
#	 [7, 8, 9]]

B = [[3, 1, 4],
	 [1, 5, 9], 
	 [2, 6, 5]]

C = [[11, 29, 37], 
	 [29, 65, 91], 
	 [47, 99, 45]] 

def equals(C, A, B):
	n = len(C)
	X = []
	#Select the rows we are going to use
	for i in range(n):
		rand = random.randint(0, 1)
		if rand == 0:
			X.append(0)
		else:
			X.append(1)
	XA = []
	for i in range(n):
		XA.append(0)
		for j in range(n):
			if X[j] == 1:
				XA[i] += A[i][j]
	XAB = []
	for i in range(n):
		XAB.append(0)
		for j in range(n):
			XAB[i] += XA[j] * B[i][j]

	XC = []
	for i in range(n):
		XC.append(0)
		for j in range(n):
			if X[j] == 1:
				XC[i] += C[i][j]

	for i in range(n):
		if XC[i] != XAB[i]:
			return False

	return True

print(equals(C, A, B))


