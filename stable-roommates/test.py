import matchmaker,matrices,result
from stats import GroupStat

for i in range(4,25):
	group_stat = GroupStat(i)
	for j in range(0,4):		
		prefs = matrices.random_matrix(i)
		res = matchmaker.execute(prefs,False)
		res.statify(group_stat)
		res.print_nicely(i)
GroupStat.print_nicely()
