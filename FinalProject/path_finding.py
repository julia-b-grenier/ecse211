#!/usr/bin/env python3

""" 
Version 1 - Implement finding the path to follow and return a list of action from the inputted coordinates
"""

import math
from collections import deque

#=-=-=-=-=-=- Initialization of variables -=-=-=-=-=-=#
listOfInstruction = []
localPosition = [0,0] #robots starts at 0,0
localRotation = 0 #robot start at 0 looking toward 0,3
fireLocations = []
fireMatrix = []


#=-=-=-=-=-=- Main path finding function -=-=-=-=-=-=#
def getInstructionList(coordinatesArray):
	global listOfInstruction
	global fireLocations
	global localPosition
	global fireMatrix

	#fireLocation is used to keep track which fire we took care of
	#coordinatesArray is used to keep a list of all the fires
	fireLocations = coordinatesArray[:]
	fireMatrix = constructMatrix(coordinatesArray)
	
	while len(fireLocations) != 0:
		closestFire = getClosestFire(fireLocations, localPosition)
		localPosition = goToFire(coordinatesArray, localPosition, closestFire)
		fireLocations.remove(closestFire) #keeping track which fires have been taken care of

	goToOrigin(coordinatesArray, localPosition)

	return listOfInstruction
#=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#=-=-=-=-=-=-=-=-= Helper functions =-=-=-=-=-=-=-=-=#
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
	return 0 <= x < 4 and 0 <= y < 4 and fireMatrix[x][y] == 0 and not visited[x][y]

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

def goToFire(coordinatesArray, position, fireCoordinate):
	global listOfInstruction
	global fireMatrix

	path = bfs(fireMatrix, localPosition[0], localPosition[1], fireCoordinate[0], fireCoordinate[1])
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

def goToOrigin(coordinatesArray, position):
	path = bfs(fireMatrix, localPosition[0], localPosition[1], 0, 0)
	path.append((0,0))

	for coordinate in path:
		if position != coordinate :
			rotateTowards(position, coordinate)
			listOfInstruction.append("FWD")
			position = coordinate

	rotateTowards(position, [0,1])

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
#=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=#