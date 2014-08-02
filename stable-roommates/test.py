# runs multiple tests on the matching algorithm

import matchmaker,matrices,result
from stats import GroupStat

#constants...

SMALLEST_GROUP = 40
LARGEST_GROUP = 80

INCREMENT = 2

TESTS_PER_GROUP_SIZE = 8

# iterate over all group sizes in the testing range
for group_size in range(SMALLEST_GROUP,LARGEST_GROUP+1,INCREMENT):

	#create a GroupStat object for this group size
	group_stat = GroupStat(group_size)

	#and start testing...
	for test_number in range(0,TESTS_PER_GROUP_SIZE):		

		#generate a random matrix, execute the tests
		prefs = matrices.random_matrix(group_size)
		res = matchmaker.execute(prefs,False)
		
		# statify and print the results!
		res.statify(group_stat)
		res.print_nicely(group_size)

#print out the GroupStat object
GroupStat.print_nicely()
