import matchmaker,matrices

# standard stable roommate preference array (from wikipedia)
# prefs = tests.wiki_roommate

# standard stable marriage preference array (from rosetta code)
# prefs = tests.rosetta_marriage

# random preference array generator in tests.py
prefs = matrices.random_matrix(4)

matchmaker.execute(prefs,True)