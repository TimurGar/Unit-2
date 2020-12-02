# AdventofCode
## Day 1
### Part one
My code:
```.py
# Advent code day 1
# My solution:

  database = open("Advent code 1_input.txt","r").read().splitlines()
  int_db =[]
  for n in range(len(database)):
      int_db.append(int(database[n]))
  print(int_db)

  for i in range(len(int_db)):
      for y in range(len(int_db)):
          if i != y and int_db[i] + int_db[y] == 2020:
              print(int_db[i],int_db[y])
              print(int_db[i] * int_db[y])
            
```
## Solution:
Correct pair of numbers is **456** and **1564**. The multiplication of this two numbers is **713184**

### Part two
```.py
# Advent code day 1
# My solution:

database = open("Advent code 1_input.txt","r").read().splitlines()
int_db =[]
for n in range(len(database)):
    int_db.append(int(database[n]))
print(int_db)

for i in range(len(int_db)):
    for y in range(len(int_db)):
        for z in range(len(int_db)):
            if i != y and y != z and int_db[i] + int_db[y] + int_db[z] == 2020:
                print(int_db[i],int_db[y],int_db[z])
                print(int_db[i] * int_db[y] * int_db[z])
 ```
 Correct pair of numbers is **764** , **857** and **399**. The multiplication of this two numbers is **261244452**

 
 
