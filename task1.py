def Fibonacci_series(Number):
  if(Number == 0):
    return 0
  elif(Number == 1):
    return 1
  else:
    return (Fibonacci_series(Number - 2) + Fibonacci_series(Number - 1))

n = int(input("Enter the value of n: "))
print("Fibonacci Series:", end = ' ')
for n in range(0, n):
  print(Fibonacci_series(n), end = ' ')
