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

total_num = 0

#original stats
total_len = 0
worst_path_and_cooridates = [[],[]]

#new stats
new_total_len = 0
new_worst_path_and_cooridates = [[],[]]

#new stats
ta_total_len = 0
ta_worst_path_and_cooridates = [[],[]]

for coordinates_fire in all_selections:
	print(coordinates_fire)
	path = path_finding.getInstructionList(coordinates_fire)
	shortPath = path_finding.getShorterInstructionList(coordinates_fire)
	TA_path = path_finding.getTAInstructionList(coordinates_fire)
	if shortPath:
		total_num += 1
		total_len += len(path)
		new_total_len += len(shortPath)
		ta_total_len += len(TA_path)
		if len(ta_worst_path_and_cooridates[1]) < len(TA_path):
			ta_worst_path_and_cooridates = [coordinates_fire, TA_path]
		if len(worst_path_and_cooridates[1]) < len(path):
			worst_path_and_cooridates = [coordinates_fire, path]
		if len(new_worst_path_and_cooridates[1]) < len(shortPath):
			new_worst_path_and_cooridates = [coordinates_fire, shortPath]

print("number of fires:", len(all_selections))
print("number of possible fires:", total_num)
print("average number of instructions for old algorithm:", total_len/total_num)
print("average number of instructions for new algorithm:", new_total_len/total_num)
print("average number of instructions for TA algorithm:", ta_total_len/total_num)
print("worst path:", worst_path_and_cooridates)
print("new worst path:", new_worst_path_and_cooridates)
print("TA worst path:", ta_worst_path_and_cooridates)

