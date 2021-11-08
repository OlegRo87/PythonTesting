file = open('test.txt')
# print(file.read())
# print(file.read(5))  # 5 characters
# print(file.readline())  # read one  line


#  print line by line

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()


for line in file.readlines():
    print(line)








file.close()
