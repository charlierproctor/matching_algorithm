# Stable Roommates Matching Algorithm

This is an implementation of the stable roommates algorithm, inspired by none other than [https://en.wikipedia.org/wiki/Stable_roommates_problem](https://en.wikipedia.org/wiki/Stable_roommates_problem).

The algorithm has been developed and tested using Python 2.7.

## Usage

For immediate results:

```bash
python match.py
python test.py
```

To run the algorithm on a given preference matrix, run `matchmaker.execute(matrix)`. For example,

```python
# random preference array generator in tests.py
prefs = matrices.random_matrix(20)

# execute the match!!
matchmaker.execute(prefs)
```

Examples such as this are contained in the `match.py` executable. Feel free to run it and play with the results.

`test.py` runs a series of tests, displaying the results in a nicer format.

## Layout

The core of the matching occurs in the `matchmaker.py` file. `match.py` is meant to be the executable, from which you can test the other methods. `person.py` contains the definition of a `Person` class, which allows for proposal to/from another, etc.

The rest of the files are for testing / exploration purposes:

- `matrices.py` contains a variety of common preference matrix options (such as random, wikipedia, and rosetta code).
- `result.py` contains the `Result` class, which attempts to format results nicely
- `stats.py` tracks the statistics of a particular matching run.
- `test.py` runs the algorithm on a series of matrices of varying sizes, displaying the results as appropriate.