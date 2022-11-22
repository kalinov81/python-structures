A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
B = ['a', 'b', 'c', 'a', 'a', 'b', 'c', 'a', 'b', 'c']

def groupbysum(A, B) -> dict:
	dt = {}
	for i, j in zip(A, B):
		dt[j] = dt.get(j, 0) + i
	return dt
	
print(groupbysum(A, B))
  
  
