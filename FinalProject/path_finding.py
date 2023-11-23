#!/usr/bin/env python3

""" 
Version 1 - Implement finding the path to follow and return a list of action from the inputed coordinates
"""

from collections import deque

#=-=-=-=-=-=- Initialization of variables -=-=-=-=-=-=#
listOfInstruction = []
localPosition = [0,0] #robots starts at 0,0
localRotation = 0 #robot start at 0 looking toward 0,3
fireLocations = []
fireMatrix = []

#=-=-=-=-=-=- Main path finding function -=-=-=-=-=-=#
def getDepInstructionList(coordinatesArray):
	global listOfInstruction
	global fireLocations
	global localPosition

	#fireLocation is used to keep track which fire we took care of
	#coordinatesArray is used to keep a list of all the fires
	initialization(coordinatesArray)
	
	while len(fireLocations) != 0:
		closestFire = getClosestFire(fireLocations, localPosition)
		localPosition = goToFire(localPosition, closestFire)
		fireLocations.remove(closestFire) #keeping track which fires have been taken care of

	goToOrigin(localPosition)

	return listOfInstruction

def getInstructionList(coordinatesArray):
	global listOfInstruction
	global fireLocations
	global localPosition

	all_paths = []

	#fireLocation is used to keep track which fire we took care of
	#coordinatesArray is used to keep a list of all the fires
	
	fireOrders = [
	[fireLocations[0],fireLocations[1],fireLocations[2]],
	[fireLocations[0],fireLocations[2],fireLocations[1]],
	[fireLocations[1],fireLocations[0],fireLocations[2]],
	[fireLocations[1],fireLocations[2],fireLocations[0]],
	[fireLocations[2],fireLocations[0],fireLocations[1]],
	[fireLocations[2],fireLocations[1],fireLocations[0]]]

	for fireOrder in fireOrders:
		initialization(coordinatesArray)
		
		for fire in fireOrder:
			localPosition = goToFire(localPosition, fire)

		goToOrigin(localPosition)

		all_paths.append(listOfInstruction)

	shortestPath = all_paths[0]
	for path in all_paths:
		if len(shortestPath) > len(path):
			shortestPath = path

	return shortestPath

def getShorterInstructionList(coordinatesArray):
	global listOfInstruction
	global fireLocations
	global localPosition

	#fireLocation is used to keep track which fire we took care of
	#coordinatesArray is used to keep a list of all the fires
	initialization(coordinatesArray)
	
	localPosition = goToFiresWithBbfs(localPosition)

	if not localPosition:
		print("fire not reachable")
		return False

	goToOrigin(localPosition)

	return listOfInstruction	
#=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#=-=-=-=-=-=-=-=-= Helper functions =-=-=-=-=-=-=-=-=#
def initialization(coordinatesArray):
	global listOfInstruction
	global fireLocations
	global localRotation
	global localPosition
	global fireMatrix

	listOfInstruction = []
	localPosition = [0,0] #robots starts at 0,0
	localRotation = 0 #robot start at 0 looking toward 0,3
	fireLocations = coordinatesArray[:]
	fireMatrix = constructMatrix(coordinatesArray)

def constructMatrix(coordinatesArray):
	matrix = [
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]
	]

	for fire in coordinatesArray:
		matrix[fire[0]][fire[1]] = 1

	return matrix

def getClosestFire(coordinatesArray, position):
	closestCoordinate = coordinatesArray[0]
	for coordinate in coordinatesArray:
		if ortDistance(coordinate, position) < ortDistance(closestCoordinate, position):
			closestCoordinate = coordinate

	return closestCoordinate

def is_valid_move(x, y, visited):
	global fireMatrix
	return 0 <= x < 4 and 0 <= y < 4 and fireMatrix[x][y] == 0 and not visited[y][x]

def check_if_arrived_at_target(x,y, targets, targets_passed):
	for targetPassedCoord in targets_passed:
		if x == targetPassedCoord[0] and y == targetPassedCoord[1]:
			return False
	for targetCoord in targets:
		if x == targetCoord[0] and y == targetCoord[1]:
			return targetCoord

	return False

def has_targets_all_been_passed(passed_targets, targets):
	for target in targets:
		if not(targets in passed_targets):
			return False
	return True
		

def bfs(grid, start_x, start_y, target_x, target_y):
	visited = [[False for _ in range(4)] for _ in range(4)]
	queue = deque([(start_x, start_y, [])])  # (x, y, path)

	while queue:
		x, y, path = queue.popleft()
		visited[y][x] = True

		if x == target_x and y == target_y:
			return path

		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			new_x, new_y = x + dx, y + dy
			if is_valid_move(new_x, new_y, visited) or (new_x, new_y) == (target_x, target_y):
				new_path = path + [(x, y)]
				queue.append((new_x, new_y, new_path))

	return []  # Target is not reachable

#targets should be in the following format: [[target1_x, target1_y], [target2_x, target2_y], etc...]
def bbfs(grid, start_x, start_y, targets):
	#queue = deque([(start_x, start_y, [], [])])  # (x, y, path, targets_passed)
	#num_targets = 0
	next_queue = [(start_x, start_y, [], [])]

	while len(next_queue) > 0 and len(targets) > len(next_queue[0][3]):
		queue = deque([next_queue.pop(0)])
		visited = [[False for _ in range(4)] for _ in range(4)]
		#next_queue = []
		while queue:
			x, y, path, targets_passed = queue.popleft()
			#print(x, y, path, targets_passed)
			visited[y][x] = True

			is_at_target = check_if_arrived_at_target(x,y,targets, targets_passed)
			if is_at_target:
				new_passed = targets_passed[:]
				new_passed.append(is_at_target)
				new_path = path + [(x, y)]
				x,y = path[-1]
				next_queue.append((x,y,new_path,new_passed))
			
			else:
				for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
					new_x, new_y = x + dx, y + dy
					if is_valid_move(new_x, new_y, visited) or check_if_arrived_at_target(new_x,new_y,targets, targets_passed):
						new_path = path + [(x, y)]
						queue.append((new_x, new_y, new_path, targets_passed))
		#num_targets += 1
	return next_queue


def goToFire(position, fireCoordinate):
	global listOfInstruction
	global fireMatrix

	path = bfs(fireMatrix, localPosition[0], localPosition[1], fireCoordinate[0], fireCoordinate[1])
	if path == []:
		print("A fire is not reachable")
		return [0,0]
	path.pop(0)

	for coordinate in path:
		if position != coordinate :
			rotateTowards(position, coordinate)
			listOfInstruction.append("FWD")
			position = coordinate

	rotateTowards(position, fireCoordinate)
	#Instructions to put out the fire
	listOfInstruction.append("creepFWD")
	listOfInstruction.append(fireCoordinate[2])
	listOfInstruction.append("creepBWD")
	return position

def goToFiresWithBbfs(position):
	global listOfInstruction
	global fireMatrix

	paths = bbfs(fireMatrix, localPosition[0], localPosition[1], fireLocations)

	if len(paths) == 0:
		return False

	#finding shortest path
	shortestPath = paths[0]
	for path in paths:
		if len(shortestPath[2]) > len(path[2]):
			shortestPath = path
	shortestPath = shortestPath[2]
	shortestPath.pop(0)

	# print(shortestPath)
	for coordinate in shortestPath:
		isFire = False
		for fireCoordinate in fireLocations:
			# print(coordinate, fireCoordinate)
			if coordinate[0] == fireCoordinate[0] and coordinate[1] == fireCoordinate[1]:
				rotateTowards(position, fireCoordinate)
				#Instructions to put out the fire
				listOfInstruction.append("creepFWD")
				listOfInstruction.append(fireCoordinate[2])
				listOfInstruction.append("creepBWD")
				isFire = True
		if position != coordinate and not isFire and (coordinate != (0,0)):
			rotateTowards(position, coordinate)
			listOfInstruction.append("FWD")
			position = coordinate

	return position

def goToOrigin(position):
	path = bfs(fireMatrix, localPosition[0], localPosition[1], 0, 0)
	path.append((0,0))

	for coordinate in path:
		if position != coordinate :
			rotateTowards(position, coordinate)
			listOfInstruction.append("FWD")
			position = coordinate

	# rotateTowards(position, [0,1])

def ortDistance(coordinate1, coordinate2):
	return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])

def rotateTowards(position, destination):
	global listOfInstruction
	global localRotation

	if position[0]-destination[0] < 0: #destination is on the right
		while localRotation - 90 != 0:
			if localRotation == 0:
				listOfInstruction.append("right")
				localRotation = 90
			else:
				listOfInstruction.append("left")
				localRotation -= 90
		
	elif position[0]-destination[0] > 0: #destination is on the left
		while localRotation - 270 != 0:
			if localRotation == 0:
				listOfInstruction.append("left")
				localRotation = 270
			else:
				listOfInstruction.append("right")
				localRotation += 90

	elif position[1]-destination[1] > 0: #destination is on the bottom
		while localRotation - 180 != 0:
				if localRotation == 270:
					listOfInstruction.append("left")
					localRotation = 180
				else:
					listOfInstruction.append("right")
					localRotation += 90

	else: #destination is on the top (we assume that the given position != destination)
		while localRotation != 0:
				if localRotation == 270:
					listOfInstruction.append("right")
					localRotation = 0
				else:
					listOfInstruction.append("left")
					localRotation -= 90
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#=-=-=-=-=-=-=-=-=-=- Debugging -=-=-=-=-=-=-=-=-=-=#
if __name__ == "__main__":
	print(getShorterInstructionList([[2, 0, 'red'], [2, 1, 'red'], [1, 1, 'red']]))
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print(getTAInstructionList([[2, 0, 'red'], [2, 1, 'red'], [1, 1, 'red']]))
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print(getInstructionList([[2, 0, 'red'], [2, 1, 'red'], [1, 1, 'red']]))

	# initialization([[2, 1, 'red'], [3, 2, 'red'], [3, 3, 'red']])

	# results = bbfs(fireMatrix,0,0,fireLocations)

	# mini = results[0]
	# for result in results:
	# 	if len(mini[2]) > len(result[2]):
	# 		mini = result

	# print(mini)
	
	# for result in results:
	# 	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	# 	print(result)