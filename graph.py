def create_hash(arr,i,j, adjacency):
	if (i,j) not in adjacency.keys():
		temp = []
		for i1 in range(i-1,i+2):
			for j1 in range(j-1,j+2):

				if i1>=0 and j1>=0 and i1<len(arr) and j1<len(arr[i1]):

					if arr[i1][j1] == 1:
						temp.append([i1,j1])
		adjacency[(i,j)] = temp

	return adjacency

def find_connected_components(arr):
	adjacency = {}
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if arr[i][j] == 1:
				adjacency = create_hash(arr, i, j, adjacency)

	max_chain = 0
	keys = adjacency.keys()
	dis_connected = []
	for i in range(len(keys)):
		if keys[i] not in dis_connected:
			for j in range(i+1,len(keys)):
				flag = True
				if keys[j] not in dis_connected:
					for ele in adjacency[keys[j]]:
						if ele in adjacency[keys[i]]:
							flag = False
							break
					if flag == True:
						if keys[j] not in dis_connected:
							dis_connected.append(keys[j])
	print "number of connected components:", len(dis_connected) + 1
	for key,val in adjacency.iteritems():
		if len(val) > max_chain:
			max_chain = len(val)
	print "length of biggest chain: ", max_chain

arr = [[1,1,0,0],[0,1,1,0],[0,0,1,0],[1,0,0,0]]

find_connected_components(arr)
