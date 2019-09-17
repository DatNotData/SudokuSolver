# sudoku solver algorithm
# Dat Ha
# 2019/09/16


# generates a class that acts as the sudoku game board
# this class has many feature that will quickly let the solver access to the data on the grid
class Board:

	def __init__(self, data):
		# get the starting grid configuration and set it into a 2d array
		self.grid = [[int(j) for j in list(data[i*9:i*9+9])] for i in range(9)]


	# print the grid representation of the game board
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


	# get all of the numbers in a row from left to right
	def GetRow(self, row):
		return [self.grid[row][i] for i in range(9)]


	# get all the numbers in a column from top to bottom
	def GetColumn(self, column):
		return [self.grid[i][column] for i in range(9)]


	# get all numbers in a square, left to right, top to bottom
	# this function also returns the starting row and column coordinates in the grid of that square
	def GetSquare(self,square):
		row0 = (square//3) *3
		column0 = (square%3)*3

		data = sum([[self.grid[(row0)+row][(column0)+column] for column in range(3)]for row in range(3)],[])		
		
		return data, row0, column0


	# when a value at a coordinate only has 1 possible number,
	# then write that number to the grid (because it has to be that number)
	def UpdateWithPossibleNumbers(self, possibleNumbers):
		for row in range(9):
			for column in range(9):
				if len(possibleNumbers[row][column]) == 1:
					self.grid[row][column] = possibleNumbers[row][column][0]
		

	# output the solved sudo grid in the same format as the data input
	# this is used to compare with the solution (which is also in this format)
	def GetOneLineStringOutput(self):
		output = ''
		for row in self.grid:
			for value in row:
				output+=str(value)
		return output


			

class SudokuSolver:

	# possible numbers array
	# at the start, every square can be any number from 1-9 inclusively
	# then, as we refine everything, the possibilities reduce until there is only 1 possible number left
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

		# set the possible nunmbers of the starting values of the grid in
		for row in range(9):
			for column in range(9):
				if self.board.grid[row][column] != 0:
					self.possibleNumbers[row][column] = [self.board.grid[row][column]]


	# it will reduce the possibility of a number based on a list of numbers that that number can't be
	def ReducePossibilities(self, rowIndex, columnIndex, impossibleNumbers):
		if len(self.possibleNumbers[rowIndex][columnIndex]) > 1:
			for toBeRemoved in impossibleNumbers:
				try:
					self.possibleNumbers[rowIndex][columnIndex].remove(toBeRemoved)
				except ValueError:
					pass
				

	# prints all the possible numbers (used in debuging)
	def PrintPossibleNumbers(self):
		for row in range(9):
			for column in range(9):
				print(self.possibleNumbers[row][column])
			print()
		print('-------------------------------------')


	# gets all the numbers that a certain value can't be
	def GetImpossibleNumbers(self, iterable):
		impossibleNumbers = []
		iterableSet = set(iterable)
		for i in range(1,10):
			if i in iterableSet:
				impossibleNumbers += [i]
		return impossibleNumbers

	
	# check if we all the cases have a value (this does not mean that the board is legit solved)
	def IsSolved(self):
		value = False
		for row in self.board.grid:
			value |= (0 in row)
		return not value
	

	# solve the board
	def Solve(self, maxCycle=100000):
		
		# this will only cycle a maximum number of times
		# if it can't be solved, then it will fail, and there is an escape built in so the algorithm doesn't run forever
		for i in range(maxCycle):
			
			# general structure of solving algorithm
			# check what numbers are impossible for each cells in a row that aren't sure yet
			# go through each of those cells and reduce their possibilities with the numbers found from above
			# do this for all rows, columns, and squares
			# rinse and repeat until it is solved

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
			

			self.board.UpdateWithPossibleNumbers(self.possibleNumbers) # update	the board if we solved any cells
			
			if self.IsSolved(): # exit solve function once we solved it
				return i+1      # return the numbers of cycle needed


		else: # if after the set max we haven't solved it yet, escape the function with error message
			print("Failed to solve Sudoku in under %s moves, please raise max in order for alrorithm to run longer" %maxCycle)
			return -1 # return -1 to indicate error



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