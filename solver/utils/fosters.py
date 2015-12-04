from igraph import *

foster = Graph().LCF(90, [17, -9, 37, -37, 9, -17], 15)
foster.to_directed()

print "Is Directed? " + str(foster.is_directed())

for start in range(0, 90):
	for end in range(0, 90):
		if (start + 1 == end): #Don't delete this. Delete opposite direction edge
			opposite_ID = foster.get_eid(end, start, True, False)
			if opposite_ID != 1:
				foster.delete_edges([opposite_ID])
		else:
			opposite_ID = foster.get_eid(end, start, True, False)
			if opposite_ID != -1:
				current_ID = foster.get_eid(start, end, True, False)
				if current_ID != -1:
					foster.delete_edges([current_ID])
print "Number of Edges: " + str(len(foster.get_edgelist()))
print(foster.is_connected())

foster_list = foster.get_adjacency()

for sublist in foster_list:
	sublist = map(str, sublist)
	sublist_string = ' '.join(sublist)
	print(sublist_string)

#print(foster.get_edgelist())
#print(foster.get_adjacency())
