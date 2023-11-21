#=-=-=-=-=-=-=-=-=- Importing -=-=-=-=-=-=-=-=-=#
import sys
sys.path.insert(1, '../')
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

total_len = 0
total_num = 0
worst_path_and_cooridates = [[],[]]
for coordinates_fire in all_selections:
	print(coordinates_fire)
	path = path_finding.getInstructionList(coordinates_fire)
	if path:
		total_num += 1
		total_len += len(path)
		if len(worst_path_and_cooridates[1]) < len(path):
			worst_path_and_cooridates = [coordinates_fire, path]

print("number of fires:", len(all_selections))
print("number of possible fires:", total_num)
print("average number of instructions:", total_len/total_num)
print("worst_path_and_cooridates:", worst_path_and_cooridates)

