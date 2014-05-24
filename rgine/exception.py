from common import *
_logfmt = \
'''================================================================================
Level		: %s
Timestamp	: %d
Exc.Type    : %s
RuntimeMsg	: %s
Stack		: %s
'''

_stackinfo = \
'''
	Stack %s
		fname		: %s
		lineno		: %s
		func		: %s
		codectx		: %s
		index		: %s

'''

class error(Exception):
	def __init__(self, msg, exception=Exception, e_level="Exception", logfile="Exception.log"):
		self.msg = msg
		stackinfo = []
		j = 0
		if not issubclass(exception, Exception): exception = Exception
		self._exception = exception

		stack = inspect.stack()
		for i in map(list, stack):
			i[4] = "\n".join(i[4])
			t = (str(j), ) + tuple(map(str, i[1:]))
			stackinfo.append(_stackinfo%t)
			j += 1
		del stack

		log(
			_logfmt%(str(e_level), getTimestamp(), exception.__name__, msg, "".join(stackinfo)),
			str(logfile),
		)

	def __str__(self): return self._exception.__name__ + ": " + self.msg

def _main(): raise error("An Exception Is Raised!", ValueError)
if __name__ == "__main__": exit(_main())
