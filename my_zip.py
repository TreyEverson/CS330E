# Assignment 7
# Trey Everson
# RHE 323

# my_zip.py
def my_zip(*iterables):
	iterables = [iter(x) for x in iterables]

	while True:
		i = tuple(map(next, iterables))
		if i != ():
			yield i
		else:
			break

# tests for my_zip
def test_zip () :
   print("my_zip()")
   assert list(my_zip()) == []
   assert list(my_zip([])) == []
   assert list(my_zip((), ())) == []
   assert list(my_zip([2, 3])) == [(2,), (3,)]
   assert list(my_zip((2, 3), (4, 5), (6, 7))) == [(2, 4, 6), (3, 5, 7)]
   assert list(my_zip([2, 3, 4], [5, 6, 7])) == [(2, 5), (3, 6), (4, 7)]

test_zip()