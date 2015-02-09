sum_to_squares = 0
squares_to_sum = 0

for i in range(1, 101):
  sum_to_squares = sum_to_squares + i
  squares_to_sum = squares_to_sum + i*i

sum_to_squares_square = sum_to_squares * sum_to_squares

diff = sum_to_squares_square - squares_to_sum

print diff
