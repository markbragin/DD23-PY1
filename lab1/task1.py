numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90,
           -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_idx = numbers.index(None)
avg = (sum(numbers[:none_idx]) + sum(numbers[none_idx + 1:])) / len(numbers)
numbers[none_idx] = avg

print("Измененный список:", numbers)

