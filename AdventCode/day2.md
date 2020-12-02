# AdventofCode
## Day 2
### Part one and two
My code:
```.py
counter_1  = 0 #Part 1
counter_2  = 0 #Part 2

with open('AdventCode2.txt', 'r') as file:
    for i in file:
        input           = i.split(': ')
        password        = input[-1]

        validator_txt   = input[0].split(' ')

        occurence_range = validator_txt[0].split('-')

        letter          = validator_txt[-1]

        password_count  = password.count(letter)

        #Part 1
        if password_count >= int(occurence_range[0]) and password_count <= int(occurence_range[1]):
            counter_1 += 1

        #Part 2
        password_pos = [password[int(occurence_range[0])-1], password[int(occurence_range[1])-1]]
        if password_pos.count(letter) == 1:
            counter_2 += 1


    print('Solution1: ', counter_1)
    print('Solution2: ', counter_2)
```
