# Function to reverse words of string 
def rev_sentence(sentence):
	sentence = sentence.strip()
	# first split the string into word
	words = sentence.split(' ')

	# then reverse the split string list and join using space
	reverse_sentence = ' '.join(reversed(words))

	print(words)

	# finally return the joined string 

	return reverse_sentence.swapcase()   

print(rev_sentence("aWESOME is cODING      "))

print (1990 % 4)