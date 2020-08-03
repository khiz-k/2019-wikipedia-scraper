import wikipedia 
#print(wikipedia.search("Programming"))

value = input("Enter the subject you wish to research: ")

print(wikipedia.summary(value, sentences=3))
