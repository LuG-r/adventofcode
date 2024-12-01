answer = 0

with open("input.txt", "r") as in_file:
	for line in in_file:
		line = line.strip()
		first_digit = last_digit = None
		
		for char in line:
			if char.isdigit():
				if first_digit is None:
					first_digit = int(char)
				last_digit = int(char)

		if first_digit is not None and last_digit is not None:
			answer += (10 * first_digit) + last_digit

print(answer)