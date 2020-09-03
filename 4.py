letters = 'FFFFFF'

numbers = []
for letter in letters:
  number = ord(letter)
  numbers.append(number)

print(numbers)

print(sum(numbers))