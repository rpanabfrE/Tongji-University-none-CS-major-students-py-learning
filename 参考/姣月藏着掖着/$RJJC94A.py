print("Decomposition:")
n=100
while n<1000:
    units = n % 10
    tens = n // 10 % 10
    hundreds = n // 100
    if units**3+tens**3+hundreds**3==n:
        print(n)
    n+=1
