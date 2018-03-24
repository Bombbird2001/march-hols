#Yeah I kind of cheated
import itertools

def gen_passcode(keyword):
	"""
	Generates a list of possible permutations of the characters in a string.
    Args:
        keyword: string
            String of characters to generate permutations from

    Returns:
        A list, which contains all possible permutations
    """

    # Add your code below
	keyword = keyword.lower()
	combis = itertools.permutations(keyword, len(keyword))
	permuList = []
	for tuples in combis:
		tempList = []
		for letter in tuples:
			tempList.append(letter)
		word = ''.join(tempList)
		if not (word in permuList):
			permuList.append(word)
	return permuList

if __name__ == "__main__":
	print("The string is 'Kleen'")
	print('\n'.join(gen_passcode('Kleen')))
	

	# Add tests below
	print("The string is 'Python'")
	print('\n'.join(gen_passcode('Python')))
	
	print("The string is 'Chem'")
	print('\n'.join(gen_passcode('Chem')))
	
	print("The string is 'Baaa'")
	print('\n'.join(gen_passcode('Baaa')))