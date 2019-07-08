from ab import discountper

def test_percentage_calculation():
	percentage = discountper(10000,5000)
	assert percentage == 50
	percentage = discountper(0,5)
	assert percentage == "total is less than or equal to zero"
	percentage = discountper("5","6")
	assert percentage == "invalid arguements" 
