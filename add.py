def Add(text):
	numbers = text.split(',')
	if len(numbers) == 1:
		return int(numbers[0])
	if len(numbers) == 2:
		return int(numbers[0]) + int(numbers[1])
	else:
		return int(numbers[0]) + int(numbers[1]) + int(numbers[2])
