#=-=-=-=-=-=-=-=-=- Importing -=-=-=-=-=-=-=-=-=#
import sys
sys.path.insert(1, '/Users/Emilien/Desktop/ecse211/ecse211/FinalProject')
import path_finding
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

color_array = ["purple", "blue", "green", "yellow", "orange", "red"]
total_array = []
all_selections = []

#Loop through all possible combinations of coordinates
for i in range(0,4):
	for j in range (0,4):
		total_array.append([i,j,"red"])

for i in range(1, len(total_array)-2):
	for j in range(i+1, len(total_array)-1):
		for k in range(j+1, len(total_array)):
			all_selections.append([total_array[i],total_array[j],total_array[k]])

for coordinates_fire in all_selections:
	print(coordinates_fire)
	print(path_finding.getInstructionList(coordinates_fire))

print(total_array)
coordinates_fire = [[1,1,"red"], [2,2,"red"], [3,3,"red"]]
instructionList = path_finding.getInstructionList(coordinates_fire)
print(instructionList)

