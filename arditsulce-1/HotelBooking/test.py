for i in range(1, 100, 1):
  temp_print = ""
  if i % 5 == 0:
    temp_print = 'Fizz'
    if i % 7 == 0:
      temp_print = 'FizzBuzz'
  elif i % 7 == 0:
    temp_print = 'Buzz'
  else:
    temp_print = i
  print(temp_print)