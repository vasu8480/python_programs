my_str="hi i am Vasu" # output: am hi i Vasu
words=[words.lower() for words in my_str.split()]
words.sort()
print("The sorted words are:")
for word in words:
	print(word,end=" ")
