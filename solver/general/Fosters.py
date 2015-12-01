from igraph import *

# foster = Graph().LCF(90, [17, -9, 37, -37, 9, -17], 15)
# foster.to_directed()

# #print "Is Directed? " + str(foster.is_directed())

# for start in range(0, 90):
# 	for end in range(0, 90):
# 		if (start + 1 == end): #Don't delete this. Delete opposite direction edge
# 			opposite_ID = foster.get_eid(end, start, True, False)
# 			if opposite_ID != 1:
# 				foster.delete_edges([opposite_ID])
# 		else:
# 			opposite_ID = foster.get_eid(end, start, True, False)
# 			if opposite_ID != -1:
# 				current_ID = foster.get_eid(start, end, True, False)
# 				if current_ID != -1:
# 					foster.delete_edges([current_ID])
# #print "Number of Edges: " + str(len(foster.get_edgelist()))
# #print(foster.is_connected())

# foster_list = foster.get_adjacency()

# for sublist in foster_list:
# 	sublist = map(str, sublist)
# 	sublist_string = ' '.join(sublist)
# 	print(sublist_string)

# for i in range(0,50):
# 	string = []]
# 	for j in range(0,50):
# 		if i != j:
# 			string.append(1)
# 		else:
# 			string.append(0)
# 	string = map(str, string)
# 	print(string)


#print(foster.get_edgelist())
#print(foster.get_adjacency())

franklin = Graph().LCF(12, [5, -5], 6)
franklin.to_directed()

for start in range(0, 12):
	for end in range(0, 12):
		if (start + 1 == end): #Don't delete this. Delete opposite direction edge
			opposite_ID = franklin.get_eid(end, start, True, False)
			if opposite_ID != 1:
				franklin.delete_edges([opposite_ID])
		else:
			opposite_ID = franklin.get_eid(end, start, True, False)
			if opposite_ID != -1:
				current_ID = franklin.get_eid(start, end, True, False)
				if current_ID != -1:
					franklin.delete_edges([current_ID])

franklin_list = franklin.get_adjacency()

for sublist in franklin_list:
	sublist = map(str, sublist)
	sublist_string = ' '.join(sublist)
	print(sublist_string)



print("SEPARATE")

headwood = Graph().LCF(14, [5, -5], 7)
headwood.to_directed()

for start in range(0, 14):
	for end in range(0, 14):
		if (start + 1 == end): #Don't delete this. Delete opposite direction edge
			opposite_ID = headwood.get_eid(end, start, True, False)
			if opposite_ID != 1:
				headwood.delete_edges([opposite_ID])
		else:
			opposite_ID = headwood.get_eid(end, start, True, False)
			if opposite_ID != -1:
				current_ID = headwood.get_eid(start, end, True, False)
				if current_ID != -1:
					headwood.delete_edges([current_ID])

headwood_list = headwood.get_adjacency()

for sublist in headwood_list:
	sublist = map(str, sublist)
	sublist_string = ' '.join(sublist)
	print(sublist_string)




