answer = 0
map = {
	"zero": 0,
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}

with open("test2.txt", "r") as in_file:
	for line in in_file:
		line = line.strip()
		first_digit = last_digit = None
		running_string = ""

		for character in line:
			if character.isdigit():
				if first_digit is None:
					first_digit = int(character)
				last_digit = int(character)
			else:
				running_string += character
				if running_string in map:
					if first_digit is None:
						first_digit = map[running_string]
					last_digit = map[running_string]
					running_string = ""
		print(f"{first_digit}{last_digit}")
		if first_digit is not None and last_digit is not None:
			answer += (10 * first_digit) + last_digit

print(answer)