class Board:

	def __init__(self, data):
		self.grid = [[int(j) for j in list(data[i*9:i*9+9])] for i in range(9)]


	def Print(self):
		print("Sudoku grid")
		for row in range(9):
			if(row%3)==0:
				print('-------------')
			for column in range(9):
				if(column%3)==0:
					print('|', end='')
				print(self.grid[row][column], end='')
			print('|')
		print('-------------')
		print()	


	def GetRow(self, row):
		return [self.grid[row][i] for i in range(9)]


	def GetColumn(self, column):
		return [self.grid[i][column] for i in range(9)]


	def GetSquare(self,square):
		row0 = (square//3) *3
		column0 = (square%3)*3

		data = sum([[self.grid[(row0)+row][(column0)+column] for column in range(3)]for row in range(3)],[])		
		
		return data, row0, column0


	def UpdateWithPossibleNumbers(self, possibleNumbers):
		for row in range(9):
			for column in range(9):
				if len(possibleNumbers[row][column]) == 1:
					self.grid[row][column] = possibleNumbers[row][column][0]
		

	def GetOneLineStringOutput(self):
		output = ''
		for row in self.grid:
			for value in row:
				output+=str(value)
		return output


			

class SudokuSolver:

	possibleNumbers = [
		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],
		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],
		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],

		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],
		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],
		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],

		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],
		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],
		[[1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],  [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9],],
	]


	def __init__(self, board):
		self.board = board

		for row in range(9):
			for column in range(9):
				if self.board.grid[row][column] != 0:
					self.possibleNumbers[row][column] = [self.board.grid[row][column]]


	def ReducePossibilities(self, rowIndex, columnIndex, impossibleNumbers):
		if len(self.possibleNumbers[rowIndex][columnIndex]) > 1:
			for toBeRemoved in impossibleNumbers:
				try:
					self.possibleNumbers[rowIndex][columnIndex].remove(toBeRemoved)
				except ValueError:
					pass
				

	def PrintPossibleNumbers(self):
		for row in range(9):
			for column in range(9):
				print(self.possibleNumbers[row][column])
			print()
		print('-------------------------------------')


	def GetImpossibleNumbers(self, iterable):
		impossibleNumbers = []
		iterableSet = set(iterable)
		for i in range(1,10):
			if i in iterableSet:
				impossibleNumbers += [i]
		return impossibleNumbers

	
	def IsSolved(self):
		value = False
		for row in self.board.grid:
			value |= (0 in row)
		return not value
	

	def Solve(self, maxCycle=100000):
		for i in range(maxCycle):
			for rowIndex in range(9):
				row = self.board.GetRow(rowIndex)
				impossibleNumbers = self.GetImpossibleNumbers(row)
				for columnIndex in range(9):
					self.ReducePossibilities(rowIndex, columnIndex, impossibleNumbers)
			
			for columnIndex in range(9):
				column = self.board.GetColumn(columnIndex)
				impossibleNumbers = self.GetImpossibleNumbers(column)
				for rowIndex in range(9):
					self.ReducePossibilities(rowIndex, columnIndex, impossibleNumbers)

			
			for squareIndex in range(9):
				square, row0, column0 = self.board.GetSquare(squareIndex)
				impossibleNumbers = self.GetImpossibleNumbers(square)
				for rowIndex in range(3):
					for columnIndex in range(3):
						self.ReducePossibilities(row0 + rowIndex, column0 + columnIndex, impossibleNumbers)
			
			self.board.UpdateWithPossibleNumbers(self.possibleNumbers)
			if self.IsSolved():
				return i+1
		else:
			print("Failed to solve Sudoku in under %s moves, please raise max in order for alrorithm to run longer" %maxCycle)
			return -1



puzzle   = '062030710790080046000000900040002090605000030900150820400800200003014580800507000'
solution = '562439718791285346384761952148372695625948137937156824456893271273614589819527463'
solver = SudokuSolver(Board(puzzle))


cycles = solver.Solve()
print(cycles)

#solver.board.Print()
#Board(solution).Print()


print(puzzle)
print(solver.board.GetOneLineStringOutput())
print(solution)
print(solver.board.GetOneLineStringOutput() == solution)
print('--------------------------------------')