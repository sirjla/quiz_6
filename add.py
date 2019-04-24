def Add(text):
	numbers = text.split(',')
	numbers = filter(lambda number: number != '', numbers)
	numbers = filter(lambda number: str.isdigit(number), numbers)
	numbers = map(int, numbers)
	numbers = filter(lambda number: number>0, numbers)
	return sum(numbers)
