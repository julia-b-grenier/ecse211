import math

#=-=-=-=-=-=- Initialization of variables -=-=-=-=-=-=#
listOfInstruction = []
localPosition = [0,0] #robots starts at 0,0
localRotation = 0 #robot start at 0 looking toward 0,3
fireLocations = []


#=-=-=-=-=-=- Main path finding function -=-=-=-=-=-=#
def getInstructionList(coordinatesArray):
	global fireLocations
	global localPosition

	#fireLocation is used to keep track which fire we took care of
	#coordinatesArray is used to keep a list of all the fires
	fireLocations = coordinatesArray[:]
	
	while len(fireLocations) != 0:
		closestFire = getClosestFire(fireLocations, localPosition)
		localPosition = goToFire(coordinatesArray, localPosition, closestFire)
		fireLocations.remove(closestFire) #keeping track which fires have been taken care of

	goToOrigin(coordinatesArray, localPosition)
#=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#=-=-=-=-=-=-=-=-= Helper functions =-=-=-=-=-=-=-=-=#
def getClosestFire(coordinatesArray, position):
	closestCoordinate = coordinatesArray[0]
	for coordinate in coordinatesArray:
		if distance(coordinate, position) < distance(closestCoordinate, position):
			closestCoordinate = coordinate

	return closestCoordinate

def goToFire(coordinatesArray, position, fireCoordinate):
	global listOfInstruction

	#while we are not one box away
	while distance(fireCoordinate, position) > 1:
		while position[1] 


	#Instructions to rotate the robot towards the fire
	rotateTowards(position, fireCoordinate)
	#Instructions to put out the fire
	listOfInstruction.append("creepFWD")
	listOfInstruction.append(fireCoordinate[2])
	listOfInstruction.append("creepBWD")

	return position

def goToOrigin(coordinatesArray, position):
	

def distance(coordinate1, coordinate2):
	return abs(coordinate1[0] - coordinate1[0]) + abs(coordinate1[1] - coordinate1[1])

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

	elif position[1]-destination[1] < 0: #destination is on the bottom
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