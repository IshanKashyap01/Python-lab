def detect_spam(phrase):
	
	phrases = ["buy now", "make a lot of money", "subscribe this", "click this"]
	for i in phrases:
		if i in phrase:
			return True
	
	return False

comment = input("Enter your comment: ")
if(detect_spam(comment)):
	print("The comment is a spam")
else:
	print("The comment isn't a spam")
