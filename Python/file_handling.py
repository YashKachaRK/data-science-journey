# open file
# file = open('data.txt', 'r')

# read file
# content = file.read()
# print(content)


# for line in file:
#     print(line)

# lines = file.readlines()
# print(lines)

# file.close()



# file = open("data.txt", "w")
# file.write("Hello Data Science\n")
# file.close()


# file = open("data.txt", "a")
# file.write("Python File Handling\n")
# file.close()

# import csv

# with open("matches.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
import csv

data = [
    ["Name", "Age"],
    ["Yash", 21],
    ["Amit", 22]
]

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
