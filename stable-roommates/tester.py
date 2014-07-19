# generates a random preference matrix

import random, pprint

class Tester:
	def random_list(length,current):
		arr = []
		nums = list(range(1,length+1))
		nums.remove(int(current))
		for i in range(length-1):
			next_num = random.choice(nums)
			arr.append(str(next_num))
			nums.remove(next_num)
		return arr

	def random_matrix(num_elem):
		res = {}
		for i in range(1,num_elem+1):
			res[str(i)] = Tester.random_list(num_elem,i)
		return res
