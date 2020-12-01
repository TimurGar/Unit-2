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




