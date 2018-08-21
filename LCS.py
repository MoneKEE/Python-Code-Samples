#! python2
# coding: utf-8

def get_LCS_Length(s1,s2):
	m = len(s1)
	n = len(s2)
	
	matrix = [[0 for x in range(m)] for y in range(n)]
	
	for x in range(1,m):
		for y in range(1,n):
			if s1[x-1] == s2[y-1]:
				matrix[x][y] = matrix[x-1][y-1] + 1
			elif matrix[x-1][y] >= matrix[x][y-1]:
				matrix[x][y] = matrix[x-1][y]
			else:
				matrix[x][y] = matrix[x][y-1]
	
	result = matrix[m-1][n-1]
	return result

def largest_common_string():
	first_string = raw_input("First string: ")
	second_string = raw_input("Second string: ")
	
	get_LCS_Length(first_string,second_string)
