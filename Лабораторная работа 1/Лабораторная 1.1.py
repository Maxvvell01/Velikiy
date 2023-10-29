numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0

amount_of_numbers = len(numbers)
sum_of_numbers = sum(numbers)

average_amount = round(sum_of_numbers / amount_of_numbers, 2)

numbers[4] = average_amount

print(numbers)
