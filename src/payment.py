def process_payment(amount):
	if amount > 0:
		return "Payment processed"
	else:
		return "Invalid amount"

# пример использования
print(process_payment(100))
print(process_payment(-50))
