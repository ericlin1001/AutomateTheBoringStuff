def printTD(tuples,dicts):
	"""it receives two args,  tuples, dicts."""
	for i in range(len(tuples)):
		print("tuples[" + str(i) + "] = " + str(tuples[i]), end = ', ');
	keys = sorted(dicts.keys(), key = lambda x:len(x));
	for j in keys:
		print("dicts[" + str(j) + "] = " + str(dicts[j]), end = ', ');

def foo(arg0,  *tuples,  **dicts):
	"""This is foo function, it receives any number of args."""
	print("foo.__doc__ = " + foo.__doc__);
	print("foo(arg0:"+str( arg0), end = ', ');
	printTD(tuples, dicts);
	print(")");
	bar( *tuples,  ** dicts);

def bar(arg0, arg1,  *tuples,  **dicts):
	"""This is bar function"""
	print("bar.__doc__ = " + bar.__doc__);
	print("bar(arg0:" + str(arg0) + ", arg1:" + str(arg1), end = ', ');
	printTD(tuples, dicts);
	print(")");
