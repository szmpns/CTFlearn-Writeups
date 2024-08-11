
with open("data.dat" , "r") as file:
    data  = file.readlines()

    counter = 0

    for line in data:
        if line.count('0') % 3 == 0 or line.count('1') % 2 == 0:
            counter += 1

    print(counter)