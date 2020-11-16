# Task 3
## Snakify practice

### Task: List of squares

```.py

n = int(input("Input your number: "))
x = 1
while x**2 <= n:
    print(x**2, end=" ")
    x += 1    
```

### Task: Least divisor
```.py
n = int(input("Input your number: "))
x = 2
while n % x != 0:
    x += 1
print(x)
```

### Task: Morning jog
```.py
x = int(input("Initial distance: "))
y = int(input("Target distance: "))
days = 1
while x < y:
    x = x * 110 / 100
    days += 1
print(days)
```
