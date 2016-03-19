text = open("2.txt").read()
print "".join(__import__("re").findall("[a-zA-Z]+",text))
print "".join([char for char in text if char.isalpha()])