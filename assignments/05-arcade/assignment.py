# Part 1 - figuring out whether the boss is dead
def boss_dead(t, a, x, b):
	"""
	Args:
		t: int
			The time that we want to check whether the boss is dead.
			For instance, boss_dead(10, a, x, b) returns whether the
			boss is dead 10 seconds after the game starts.
		a: int
			Interval at which Aaron deals a damage
		x: int
			Interval at which Xuanchun deals a damage
		b: int
			Amount of damage a boss can take before it is dead

	Returns:
		A boolean, where True means the boss is dead and False means the boss is not
	"""

	# Your code here
	dmg = (t + 1) // a + (t + 1) // x
	return dmg >= b

# Part 2 - figuring out when the game ends
def game_length(a, x, b):
	"""
	Args:
		a: int
			Interval at which Aaron deals a damage
		x: int
			Interval at which Xuanchun deals a damage
		b: int
			Amount of damage a boss can take before it is dead

	Returns:
		An int, the amount of time it takes for the game to be over.
	"""

	# Your code here
	t = 0
	while True:
		dmg = 0
		for i in range(t + 1):
			if (i % a == 0):
				dmg += 1
			if (i % x == 0):
				dmg += 1
		if dmg >= b:
			break
		t += 1
	
	return t

# Part 4 - optimised code using binary search
def game_length_opt(a, x, b):
	"""
	Args:
		a: int
			Interval at which Aaron deals a damage
		x: int
			Interval at which Xuanchun deals a damage
		b: int
			Amount of damage a boss can take before it is dead

	Returns:
		An int, the amount of time it takes for the game to be over.
	"""

	l = 0
	r = 10**18

	while(r - l > 1):
		guess = (r + l) // 2 # // stands for floored division
		if boss_dead(guess, a, x, b):
			r = guess
		else:
			l = guess
	return r

if __name__ == '__main__':
	print(boss_dead(0, 1, 1, 10))
	print(boss_dead(4, 1, 1, 10))
	print(boss_dead(4, 1, 6, 7))
	# Add your own tests after this line
	print(game_length(1, 1, 100))
	print(game_length_opt(1, 2, 10000))
	print(game_length_opt(2, 3, 4000))