import re # for a2_alt
import string

def a1():
	nums = []
	with open("input.txt", "r") as read_file:
		for line in read_file.readlines():
			digits = list(filter(lambda l: l.isnumeric(), line))
			num = int(digits[0] + digits[-1])
			nums.append(num)

	return sum(nums)

digit_strs = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
replace_strs = ("one1one", "two2two", "three3three", "four4four", "five5five", "six6six", "seven7seven", "eight8eight", "nine9nine")
replace_dict = dict(zip(digit_strs, replace_strs))

# ugly
def a2():
	nums = []
	with open("input.txt", "r") as read_file:
		for line in read_file.readlines():
			temp_line = line
			
			for key, value in replace_dict.items():
				temp_line = temp_line.replace(key, value)
			digits = list(filter(lambda l: l.isnumeric(), temp_line))
			num = int(digits[0] + digits[-1])
			nums.append(num)

	return sum(nums)

int_strs = list(map(str, range(1, 10)))

word_to_digit = dict()
word_to_digit.update(zip(digit_strs, int_strs))
word_to_digit.update(zip(map(lambda s: s[::-1], digit_strs), int_strs))
word_to_digit.update(zip(map(str, range(1, 10)), int_strs))

# still ugly, unfortunately
# arguably even more so
def a2_alt():
	nums = []
	with open("input.txt", "r") as read_file:
		for line in read_file.readlines():
			forward_exp = f'({"|".join(string.digits[1:])}|{"|".join(digit_strs)})'
			backward_exp = f'({"|".join(string.digits[1:])}|{"|".join(map(lambda s: s[::-1], digit_strs))})'
			m1 = re.search(forward_exp, line)
			m2 = re.search(backward_exp, line[::-1])

			n1 = m1.group(0)
			n2 = m2.group(0)

			num = int(word_to_digit[n1] + word_to_digit[n2])
			nums.append(num)
	
	return sum(nums)

print(a2_alt())
