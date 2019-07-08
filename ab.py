def discountper(total,amount):
	if (type(total) != int) and (type(amount) != int):
		return "invalid arguements"
	elif total<=0:
		return "total is less than or equal to zero"
	else:
		return (amount/total)*100

