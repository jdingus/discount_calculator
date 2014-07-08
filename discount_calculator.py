def calculate_discount(item_cost, relative_discount, absolute_discount):
	"""
	Calculate the discount price of an item in the shopping cart,
	First relative_discount is applied then absolute_discount is
	applied, final purchase price is the then returned (price)
	"""
	if relative_discount > 1. or absolute_discount > 1:
		raise ValueError("Discounts cannot be above 100%")

	if relative_discount < 0 or absolute_discount < 0:
		raise ValueError("Discounts cannot be negative!")

	price = item_cost

	discount_1 = price * relative_discount

	if discount_1 == price:
		price = 0
		return price

	price= price - discount_1
	
	discount_2 = price * absolute_discount

	if discount_2 == price:
		price = 0
		return price

	price = price - discount_2

	return price

def main():
	print calculate_discount(100,.5,1.6)


if __name__ == '__main__':
	main()