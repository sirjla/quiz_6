def Add(text):
	numbers = map(int, text.split(','))
	numbers = filter(lambda number: number>0, numbers)
	return sum(numbers)
