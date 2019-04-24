def Add(text):
	numbers = text.split(',')
	if len(numbers) == 1:
		return int(numbers[0])
	return int(numbers[0]) + int(numbers[1])