def Add(text, symbol=','):
	numbers = filter(lambda number: str.isdigit(number), text.split(symbol))
	numbers = map(int, numbers)
	numbers = filter(lambda number: number>0, numbers)
	return sum(numbers)
