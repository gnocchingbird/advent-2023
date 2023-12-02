from functools import reduce

def get_max_needed():
	with open("input.txt", "r") as read_file:
		max_needed = dict()
		for line in read_file.readlines():
			game, quantities = line.split(": ")
			game = int(game.split(" ")[-1])
			quantity_per_color = {"red": 0, "green": 0, "blue": 0}
			for game_round in quantities.split("; "):
				for color_str in game_round.split(", "):
					n, c = color_str.split()
					if int(n) > quantity_per_color[c]:
						quantity_per_color.update({c: int(n)})
			
			max_needed.update({game: quantity_per_color})

		return max_needed

def a1():
	return sum((k for k, v in get_max_needed().items() if (v["red"] <= 12 and v["green"] <= 13 and v["blue"] <= 14)))

def a2():
	return sum(map(lambda game: reduce(lambda x, y: x * y, game.values(), 1), get_max_needed().values()))

print(a2())
