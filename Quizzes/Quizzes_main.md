# Winter break homework
## Quizzes 1 - 12

### Quiz 1
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%201.jpg)
```.py
# Quiz 1
def Makes10(A,B):
    if A == 10 or B == 10 or A+B == 10:
        return True
    else:
        return False

print(Makes10(9,10))
print(Makes10(9,9))
print(Makes10(1,9))
```

### Quiz 2
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%202.jpg)
```.py
# Quiz 2
def IntMax(A,B,C):
    if B > A and B > C:
        return B
    if C > B and C > A:
        return C
    if A > B and A > C:
        return A

print(IntMax(1,2,3))
print(IntMax(1,3,2))
print(IntMax(3,2,1))
```

### Quiz 3
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%203.jpg)
```.py
# Quiz 3
def rangeN(N):
    sum = 0
    for i in range(N+1):
        print(i)
        sum += i
    print(sum)

rangeN(6)
```

### Quiz 4
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%204.jpg)
```.py
#Quiz 4
def perfectN(N):
    sum = 0
    s = False
    for i in range(1,N):
        if N % i == 0:
            print(i)
            sum += i
    if sum == N:
        s = True
    else:
        s = False
    return print("Sum of factors is:",sum,",", s)

perfectN(6)
```

### Quiz 5
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%205.jpg)
```.py
#Quiz 5
def tableM(N):
    for i in range(1,10):
        print("{}x{} = {}".format(N,i,N*i))

tableM(2)
```

### Quiz 6
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%206.jpg)
```.py
#Quiz 6
def MixStart(L):
    if L[1] == "i" and L[2] == "x":
        return True
    else:
        return False

print(MixStart("mix snacks"))
print(MixStart("pix snacks"))
print(MixStart("miz snacks"))
```
### Quiz 7
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%207.jpg)
```.py
#Quiz 7
def letters(S):
    for i in range(len(S)):
        print("{} -> {} ".format(i,S[i]))

letters("hello")
```
### Quiz 8
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%208.jpg)
```.py
# Quiz 8
def maxAbs(S):
    biggest = 0
    for i in range(len(S)):
        S[i] = abs(S[i])
        if S[i] > biggest:
            biggest = S[i]
    return print("max absolute is", biggest)

print(maxAbs([-4, 5, 6, -7]))
print(maxAbs([-1, 0, 1]))
print(maxAbs([-100, 0, 3, -200]))
```
### Quiz 9
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%209.jpg)
```.py
#Quiz 9
def missingNumber(S):
    for i in range(len(S)+ 1):
        if S[i+1] - S[i] == 2:
            return print(int((S[i+1] + S[i]) /2))

print(missingNumber([1,2,3,5,6,7]))
print(missingNumber([4,5,6,8,9,10]))
print(missingNumber([73,74,75,76,78,79]))

```
### Quiz 10
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%2010.jpg)
```.py
# Quiz 10
def BigNeighbour(S):
    d = 0
    for i in range(len(S)-1):
        if (S[i+1] - S[i]) > d:
            d = S[i+1] - S[i]
            big = S[i+1]
            small = S[i]
    return print("{}(because {} to {})".format(d,small,big))

print(BigNeighbour([1,2,3,5,6,7]))
print(BigNeighbour([0,5,6,10]))
print(BigNeighbour([73,74,174,76,78,79]))
```
### Quiz 11
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%2011.jpg)
```.py
# Quiz 11
def SameFirstLast(n):
    if len(n) >= 1 and n[0] == n[-1]:
        return True
    return False

print(SameFirstLast([1,2,3]))
print(SameFirstLast([1,2,3,1]))
print(SameFirstLast([1,2,1]))

```

### Quiz 12
![Photo](https://github.com/TimurGar/Unit-2/blob/main/Quizzes/Quiz%2012.jpg)
```.py
# Quiz 12
def wordlength(S):
    l = 0
    for i in range(len(S)):
        l += len(S[i])
    return print(l/len(S))

wordlength(["home", "car", "travel", "beach"])
wordlength(["sun", "sat", "cut", "can"])
wordlength(["police", "abacus"])
```
