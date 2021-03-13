#Original function
def square_original(num) :
  result = num ** 2

value = square_original(4)
print(value)

#Using Lambda
square = lambda num: num ** 2

value_lambda = square(2)
print(value_lambda)
