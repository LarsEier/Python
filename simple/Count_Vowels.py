def Count_Vowels(string):
	count = 0
	for i in string:
		if i in ["a", "e", "i", "o", "u"]:
			count += 1
	print(count)

Count_Vowels("Wonder if python can count how many vowels there is in this long sentence. PS it's 21")