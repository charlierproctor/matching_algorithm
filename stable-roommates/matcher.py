# Stable Roommate Algorithm
import pprint, sys, tests

from person import Person
from result import Result 

def execute(prefs, print_output, recursion_limit=10000):
	# adjust the system's recursion call depth limit
	# system default is 1000
	sys.setrecursionlimit(recursion_limit)

	# SETUP --> CREATE PERSON OBJECTS
	Person.setup(prefs)

	if print_output:
		print("Starting Preference Matrix -- Phase 0 Complete:")
		pprint.pprint(Person.prefsMatrix('current'))

	# PHASE 1

	#core of phase 1 --> everybody proposes to their top choice
	for person in Person.ppl.values():
		# before proposing, we need to make sure everybody hasn't rejected them yet!
		# this would happen iff everybody else has already received better offers...
		if len(person.current_prefs) > 0:       
			person.propose_to(person.current_prefs[0])  # propose to your top choice

	if print_output:
		print("Phase 1 Complete:")
		pprint.pprint(Person.prefsMatrix('current'))


	# PHASE 2

	#find the initial person with a second column
	current_person = Person.find_person_with_second_column()    

	num_rotations = 1    # number of rotations so far...

	# while we still have a person with a second column
	while current_person: 

		# grab their second choice preference
		current_pref = current_person.current_prefs[1]

		# and cross off that person's last preference.... 
		# which kicks off the rotation
		current_pref.cross_off(current_pref.current_prefs[-1])

		if print_output:
			print("Rotating around person " + current_person.name + 
				", with preference " + current_pref.name)
			print("Rotation #" + str(num_rotations) + ":")

			num_rotations = num_rotations + 1
			pprint.pprint(Person.prefsMatrix('current'))	

		# find another person to work with... if there is one
		current_person = Person.find_person_with_second_column()

	if print_output:
		print("Phase 2 Complete:")
		pprint.pprint(Person.prefsMatrix('current'))

		print("\nRESULTS:\n")

	ppl_without_match = Person.who_wasnt_matched()
	stable = False

	if len(ppl_without_match) > 0:
		if print_output:
			#some people weren't matched
			print("The following individuals were unmatched:")
			for unmatched in ppl_without_match:
				print(unmatched.name)
	else:
		stable = Person.was_the_match_stable()
		#whether the match was stable?

		if print_output:
			#everybody was successfully matched
			print("Everybody is matched.\n")
			if stable:
				print("The match is stable.\n")
			else:
				print("The match is NOT stable.")

	return Result(Person.ppl,ppl_without_match,stable)


# standard stable roommate preference array (from wikipedia)
# prefs = tests.wiki_roommate

# standard stable marriage preference array (from rosetta code)
# prefs = tests.rosetta_marriage

# random preference array generator in tests.py
prefs = tests.random_matrix(4)

execute(prefs,True)
