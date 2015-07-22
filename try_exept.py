d = {'x': 'skadkj'}
try:
	value = int(d['x'])
except (KeyError, TypeError, ValueError):
	value = None

print (value)
