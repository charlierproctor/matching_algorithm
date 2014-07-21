import matchmaker,matrices

for i in range(4,101):
	for j in range(0,3):
		print("Testing on Group of " + str(i) + " People:")
		prefs = matrices.random_matrix(i)
		res = matchmaker.execute(prefs,False)