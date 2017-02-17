class matrix_add:
	def __init__(self,array):
		self.array= array
	def __add__(self,other):
		if len(self.array)==len(other.array):
			row_len1 = self.array[0]
			row_len2 = other.array[1]
			for row in self.array:
				if row_len1 != len(row):
					return None
			for row in other.array:
				if row_len2 != len(row):
					return None
		newmatrix= []
		for i in range(self.array):
			row= []
			for j in range(self.array[0]):
				row.append(self.array[i][j]+other.array[i][j])
			newmatrix.append(row)
		return newmatrix

num_row= input()
num_column= input()
matrix= []
for i in range(num_row):
	row=[]
	for j in range(num_column):
		cell= input()
		row.append(cell)
		matrix.append(row)
		m1= matrix(matrix)
		m2= matrix(matrix)
		m3= matrix(matrix)
