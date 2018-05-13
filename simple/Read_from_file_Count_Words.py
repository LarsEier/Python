file = open("Self-Reliance.txt", "r")

def Count_Words(text):
	return len(text)

print(Count_Words(file.read().split()))