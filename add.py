def Add(text, symbol=','):
	numbers = text.split(symbol)
	numbers = filter(lambda number: number != '', numbers)
	numbers = filter(lambda number: str.isdigit(number), numbers)
	numbers = map(int, numbers)
	numbers = filter(lambda number: number>0, numbers)
	return sum(numbers)
