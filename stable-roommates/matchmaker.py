# Stable Roommate Algorithm
# this is where the action happens!!

import pprint, sys

from person import Person
from result import Result 

def execute(prefs, print_output=True, recursion_limit=10000):
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

	# does anybody have an empty column at the end of phase one?
	has_empty_column_after_phase_one = Person.empty_column()
	print("Empty column --> " + str(has_empty_column_after_phase_one))

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

	# who wasn't matched?
	ppl_without_match = Person.who_wasnt_matched()
	stable = False

	#if everybody was matched, was the match stable?
	if len(ppl_without_match) == 0:
		stable = Person.was_the_match_stable()

	# grab the corresponding result object
	result = Result(Person.ppl,ppl_without_match,stable,Person.prefsMatrix("initial"))

	if print_output:
		result.print_nicely()

	# HYPOTHESIS: if there is not an empty column at the end of phase one,
	# there should be a stable match --> but this is currently NOT the case
	# if (not stable) and (not has_empty_column_after_phase_one):
		# raise Exception("The match was unstable, yet there was not an empty column at the end of phase one.")

	return result
