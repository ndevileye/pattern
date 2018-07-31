import sys

def minDist(arr, n, x, y):
	min_dist = sys.maxsize

	
	for i in range(n):
		
		if arr[i] == x or arr[i] == y:
			prev = i
			break

	
	while i < n:
		if arr[i] == x or arr[i] == y:

			if arr[prev] != arr[i] and (i - prev) < min_dist :
				min_dist = i - prev
				prev = i
			else:
				prev = i
		i += 1	

	return min_dist


arr = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]
n = len(arr)
x = 5
y = 8
print ("Minimum distance between %d and %d is %d\n"%( x, y,minDist(arr, n, x, y)));
