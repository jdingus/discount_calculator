def calculate_discount(item_cost, relative_discount, absolute_discount):
	"""
	Calculate the discount price of an item in the shopping cart,
	First relative_discount is applied then absolute_discount is
	applied, final purchase price is the then returned (price)
	"""
	discount_1 = item_cost * (1-relative_discount)
	price = discount_1 * (1-absolute_discount)
	return price


def main():
	print calculate_discount(100,.1,.1)


if __name__ == '__main__':
	main()