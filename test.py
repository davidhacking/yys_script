import sys
def Start(args):
	print args
	return 1
def ImportTestCase():
	_variables = {
		'x': 1,
		'Start': Start
	}
	def testcase():
		pass
	for key in _variables.keys():
		if not hasattr(testcase, key):
			setattr(testcase, key, _variables[key])
	return testcase
if __name__ == "__main__":
	t1 = ImportTestCase()
	t2 = ImportTestCase()
	print id(t1), id(t2)
	t1.Start('t1')
	t1.Start('t2')
	pass