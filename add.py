def Add(text):
	numbers = text.split(',')
	return sum(map(int, numbers))
